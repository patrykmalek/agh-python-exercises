from utils.CommonFunction import CommonFunction
from utils.SearchFilter import SearchFilter
from enums.LibraryEnums import MenuNames, Messages
from entities.Book import Book
from entities.Menu import Menu
from entities.Option import Option
from pathlib import Path
import time


class Library:
    DEFAULT_BOOKS_FILE_PATH = Path('data', 'books.json')

    def __init__(self, login_provider, book_repository, user_repository, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.login_provider = login_provider
        self.book_repository = book_repository
        self.user_repository = user_repository
        self.books_file = books_file
        self.library_management_system = None

    def display_books(self, books_to_display=None, message=MenuNames.ALL_BOOKS.value):
        print(CommonFunction.create_bordered_string(message))
        if books_to_display is None:
            books_to_display = self.book_repository.get_books()
        if len(books_to_display) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, book in enumerate(books_to_display):
            print(f'{index + 1}.  {book}')

    def display_borrowed_books(self):
        self.display_books(self.book_repository.get_borrowed_books(), MenuNames.BORROWED_BOOKS.value)

    def display_reserved_books(self):
        self.display_books(self.book_repository.get_reserved_books(), MenuNames.RESERVED_BOOKS.value)

    def search_book(self):
        book_menu = self.create_menu_for_objects(self.book_repository.get_books(), MenuNames.SEARCH_BOOK.value,
                                                 "Wyszukaj:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        print(f"\n{selected_book}")

    def add_book(self):
        print(CommonFunction.create_bordered_string(MenuNames.ADD_BOOK.value))
        title = input("Podaj tytuł:")
        author = input("Podaj autora:")
        while True:
            isbn = input("Podaj 13 cyfrowy numer ISBN:")
            if Book.validate_isbn(isbn):
                break
            print(Messages.ISBN_INVALID.value)
        book = Book(isbn, title, author)
        if self.book_repository.add_book(book):
            print(f"{Messages.BOOK_ADDED.value}:\n{book}")
        else:
            print(f"{Messages.BOOK_ADDED_ERROR.value}:\n")

    def remove_book(self):
        book_menu = self.create_menu_for_objects(self.book_repository.get_books(), MenuNames.REMOVE_BOOK.value,
                                                 "Wybierz książkę lub wyszukaj:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        if self.book_repository.remove_book(selected_book):
            print(f"{Messages.BOOK_REMOVED.value}:\n{selected_book}")
        else:
            print(f"{Messages.BOOK_REMOVED_ERROR.value}:\n")

    def borrow_book(self):
        book_menu = self.create_menu_for_objects(self.book_repository.get_books(), MenuNames.BORROW_BOOK.value,
                                                 "Wyszukaj i wypożycz:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        


    def accept_return_book(self):
        awaiting_to_return_books = self.get_awaiting_to_return_books()
        book_menu = self.create_menu_for_objects(awaiting_to_return_books, MenuNames.REMOVE_BOOK.value,
                                                 "Wybierz książkę lub wyszukaj:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        # TODO: find book in self.books, change some values and save in self.books

    def display_readers(self):
        print(CommonFunction.create_bordered_string(MenuNames.ALL_READERS.value))
        readers_list = self.user_repository.readers
        if len(readers_list) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, reader in enumerate(readers_list):
            print(f'{index + 1}.  {reader.to_string()}')

    def search_reader(self):
        reader_menu = self.create_menu_for_objects(self.user_repository.readers,
                                                   MenuNames.SEARCH_READER.value, "Wyszukaj:")
        selected_reader = reader_menu.execute_menu_and_get_object(SearchFilter.filter_readers)
        CommonFunction.clear_view()
        print(f"\n{selected_reader}")

    def add_reader(self):
        print(CommonFunction.create_bordered_string(MenuNames.ADD_READER.value))
        library_card_number = self.generate_library_card_number()
        print('\nGenerowanie numeru karty... ')
        time.sleep(1)
        print(f'Wygenerowany numer karty: {library_card_number}')
        reader = self.login_provider.register_reader(library_card_number)
        print(f"\n{Messages.READER_ADDED.value}:\n{reader}\n")

    # FIXME: I have no better idea for it but I use it in a few places
    def create_menu_for_objects(self, objects_list, menu_name, prompt_msg):
        options = []
        for obj in objects_list:
            options.append(Option(obj.__str__(), None, obj))
        book_menu = Menu(menu_name, options, prompt_msg)
        book_menu.library = self
        book_menu.library_management_system = self.library_management_system
        book_menu.parent_menu = self.library_management_system.current_menu
        return book_menu

    def generate_library_card_number(self):
        used_cards = [reader.library_card_number for reader in self.user_repository.readers]
        next_reader_number = len(self.user_repository.readers) + 1
        while True:
            next_card_number = str(next_reader_number).zfill(4)
            next_card_number = f"LIB-{next_card_number}"
            if next_card_number not in used_cards:
                return next_card_number
            next_reader_number += 1
