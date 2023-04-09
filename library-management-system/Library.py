from CommonFunction import CommonFunction
from LibraryEnums import MenuNames, Messages
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

    def __init__(self, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.books = []
        self.borrowed_books = []
        self.reserved_books = []
        self.readers = []
        self.books_file = books_file
        self.library_management_system = None

        # Load library state from JSON file
        self.load_books()
        self.load_readers()

    def display_books(self):
        print(CommonFunction.create_bordered_string(MenuNames.ALL_BOOKS.value))
        if len(self.books) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, book in enumerate(self.books):
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
        print("Searching book...")

    def add_book(self):
        print(CommonFunction.create_bordered_string(MenuNames.ADD_BOOK.value))
        title = input("Podaj tytuł:")
        author = input("Podaj autora:")

        book = Book(title, author)
        self.books.append(book)
        self.save_books()
        print(f"{Messages.BOOK_ADDED.value}:\n{book}")

    def remove_book(self):
        book_menu = self.create_menu_for_objects(self.books, MenuNames.REMOVE_BOOK.value, "Wybierz książkę:")
        selected_book = book_menu.execute_menu_and_get_object()
        CommonFunction.clear_view()
        if selected_book in self.books:
            self.books.remove(selected_book)
            self.save_books()
        print(f"{Messages.BOOK_REMOVED.value}:\n{selected_book}")

    def borrow_book(self):
        print("Borrowing book...")

    def return_book(self):
        print("Returning book...")

    def search_reader(self):
        print("Searching reader...")

    def add_reader(self):
        print(CommonFunction.create_bordered_string(MenuNames.ADD_READER.value))
        first_name = input("Podaj imię:")
        family_name = input("Podaj nazwisko:")
        library_card_number = self.generate_library_card_number()

        print('\nGenerowanie numeru karty... ')
        time.sleep(1)
        print(f'Wygenerowany numer karty: {library_card_number}')
        reader = Reader(first_name, family_name, library_card_number)
        self.readers.append(reader)
        self.save_readers()
        print(f"\n{Messages.READER_ADDED.value}:\n{reader}\n")

    def load_books(self):
        if not os.path.getsize(self.books_file) == 0:
            with open(self.books_file, 'r') as file:
                books_dict_list = json.load(file)
            for book_dict in books_dict_list:
                self.books.append(Book.from_dict(book_dict))

    def save_books(self):
        books_dict_list = []
        for book in self.books:
            books_dict_list.append(book.to_dict())
        with open(self.books_file, 'w') as file:
            json.dump(books_dict_list, file)

    def load_readers(self):
        self.readers = self.library_management_system.login_provider.get_readers()

    def save_readers(self):
        readers_dict_list = []
        for reader in self.readers:
            readers_dict_list.append(reader.to_dict())
        with open(self.readers_file, 'w') as file:
            json.dump(readers_dict_list, file)

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
