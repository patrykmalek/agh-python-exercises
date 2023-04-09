from Book import Book
from Menu import Menu
from Option import Option
import json
import os
from pathlib import Path


class Library:
    DEFAULT_BOOKS_FILE_PATH = Path('data', 'books.json')
    DEFAULT_READERS_FILE_PATH = Path('data', 'readers.json')

    def __init__(self, books_file=DEFAULT_BOOKS_FILE_PATH, readers_file=DEFAULT_READERS_FILE_PATH):
        self.books = []
        self.borrowed_books = []
        self.reserved_book = []
        self.readers = []
        self.books_file = books_file
        self.readers_file = readers_file
        self.library_management_system = None

        # Load library state from CSV files or json?
        self.load_books()
        self.load_readers()

    def display_books(self):
        print(f"\n--------- Wyświetlanie książek ---------")
        if len(self.books) == 0:
            print("      Brak danych...      ")
        for index, book in enumerate(self.books):
            print(f'{index + 1}.  {book}')

    def search_book(self):
        print("Searching book...")

    def add_book(self):
        print(f"\n--------- Dodawanie książki ---------")
        title = input("Podaj tytuł:")
        author = input("Podaj autora:")

        book = Book(title, author)
        self.books.append(book)
        self.save_books()
        print(f"Dodano książkę: {book}")

    def remove_book(self):
        print(f"\n--------- Usuwanie książki ---------")
        book_menu = self.create_menu_for_objects(self.books, "Usuwanie książek", "Wybierz książkę do usunięcia:")
        selected_book = book_menu.execute_menu_and_get_object()
        book_menu.clear_view()
        if selected_book in self.books:
            self.books.remove(selected_book)
            self.save_books()
        print(f"Usunięto książkę: {selected_book}")

    def borrow_book(self):
        print("Borrowing book...")

    def return_book(self):
        print("Returning book...")

    def search_reader(self):
        print("Searching reader...")

    def add_reader(self):
        print("Adding reader...")

    def remove_reader(self):
        print("Removing reader...")

    def load_books(self):
        if not os.path.getsize(self.books_file) == 0:
            with open(self.books_file, 'r') as f:
                books_dict_list = json.load(f)
            for book_dict in books_dict_list:
                self.books.append(Book.from_dict(book_dict))

    def save_books(self):
        books_dict_list = []
        for book in self.books:
            books_dict_list.append(book.to_dict())

        with open(self.books_file, 'w') as f:
            json.dump(books_dict_list, f)

    def load_readers(self):
        # TODO: Add loading data from CSV or JSON file.
        pass

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
