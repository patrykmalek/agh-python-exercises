from Book import Book
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

        # Load library state from CSV files or json?
        self.load_books()
        self.load_readers()

    def display_books(self):
        print(f"\n--------- Wyświetlanie książek ---------")
        if len(self.books) == 0:
            print("      Brak danych...      ")
        for index, book in enumerate(self.books):
            print(f'{index + 1}.  "{book.title}" - \033[3m{book.author}\033[0m')

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
        print("Removing book...")

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
