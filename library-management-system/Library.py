from CommonFunction import CommonFunction
from LibraryEnums import MenuNames, Messages
from SearchFilter import SearchFilter
from Book import Book
from Menu import Menu
from Option import Option
from Reader import Reader
from pathlib import Path
import json
import os
import time


class Library:
    DEFAULT_BOOKS_FILE_PATH = Path('data', 'books.json')

    def __init__(self, login_provider, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.books = []
        # TODO: to remove, i think
        self.borrowed_books = []
        self.reserved_books = []
        #

        self.readers = []
        self.login_provider = login_provider
        self.books_file = books_file
        self.library_management_system = None

        # Load library state from JSON file
        self.load_books()
        self.load_readers()

    def display_books(self, books_to_display=None):
        print(CommonFunction.create_bordered_string(MenuNames.ALL_BOOKS.value))
        if books_to_display is None:
            books_to_display = self.books
        if len(books_to_display) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, book in enumerate(books_to_display):
            print(f'{index + 1}.  {book}')

    def display_borrowed_books(self):
        print(CommonFunction.create_bordered_string(MenuNames.BORROWED_BOOKS.value))
        if len(self.borrowed_books) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, book in enumerate(self.borrowed_books):
            print(f'{index + 1}.  {book}')

    def display_reserved_books(self):
        print(CommonFunction.create_bordered_string(MenuNames.RESERVED_BOOKS.value))
        if len(self.reserved_books) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, book in enumerate(self.reserved_books):
            print(f'{index + 1}.  {book}')

    def search_book(self):
        book_menu = self.create_menu_for_objects(self.books, MenuNames.SEARCH_BOOK.value, "Wyszukaj:")
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
        self.books.append(book)
        self.save_books()
        print(f"{Messages.BOOK_ADDED.value}:\n{book}")

    def remove_book(self):
        book_menu = self.create_menu_for_objects(self.books, MenuNames.REMOVE_BOOK.value,
                                                 "Wybierz książkę lub wyszukaj:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        if selected_book in self.books:
            self.books.remove(selected_book)
            self.save_books()
        print(f"{Messages.BOOK_REMOVED.value}:\n{selected_book}")

    def borrow_book(self):
        print("Borrowing book...")

    def accept_return_book(self):
        awaiting_to_return_books = self.get_awaiting_to_return_books()
        book_menu = self.create_menu_for_objects(awaiting_to_return_books, MenuNames.REMOVE_BOOK.value,
                                                 "Wybierz książkę lub wyszukaj:")
        selected_book = book_menu.execute_menu_and_get_object(SearchFilter.filter_books_by_title_and_author)
        CommonFunction.clear_view()
        # TODO: find book in self.books, change some values and save in self.books

    def display_readers(self):
        print(CommonFunction.create_bordered_string(
            MenuNames.ALL_READERS.value))
        if len(self.readers) == 0:
            print(
                f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, reader in enumerate(self.readers):
            print(f'{index + 1}.  {reader.to_string()}')

    def search_reader(self):
        print("Searching reader...")

    def add_reader(self):
        print(CommonFunction.create_bordered_string(MenuNames.ADD_READER.value))
        library_card_number = self.generate_library_card_number()
        print('\nGenerowanie numeru karty... ')
        time.sleep(1)
        print(f'Wygenerowany numer karty: {library_card_number}')
        reader = self.login_provider.register_reader(library_card_number)
        self.readers.append(reader)
        print(f"\n{Messages.READER_ADDED.value}:\n{reader}\n")

    def get_reserved_books(self):
        reserved_books = []
        reserved_books = SearchFilter.filter_reserved_books(self.books)
        return reserved_books

    def get_borrowed_books(self):
        borrowed_books = []
        borrowed_books = SearchFilter.filter_borrowed_books(self.books)
        return borrowed_books

    def get_awaiting_to_return_books(self):
        awaiting_to_return_books = []
        awaiting_to_return_books = SearchFilter.filter_awaiting_to_return_books(self.books)
        return awaiting_to_return_books

    def load_books(self):
        if not os.path.getsize(self.books_file) == 0:
            with open(self.books_file, 'r', encoding='utf-8') as file:
                books_dict_list = json.load(file)
            for book_dict in books_dict_list:
                self.books.append(Book.from_dict(book_dict))

    def save_books(self):
        books_dict_list = []
        for book in self.books:
            books_dict_list.append(book.to_dict())
        with open(self.books_file, 'w', encoding='utf-8') as file:
            json.dump(books_dict_list, file)

    def load_readers(self):
        self.readers = self.login_provider.get_readers()

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
        next_reader_number = len(self.readers) + 1
        next_card_number = str(next_reader_number).zfill(4)
        return f"LIB-{next_card_number}"
