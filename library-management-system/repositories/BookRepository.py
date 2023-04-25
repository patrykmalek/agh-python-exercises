from pathlib import Path
from entities.Book import Book
from utils.SearchFilter import SearchFilter
import os
import json


class BookRepository:
    DEFAULT_BOOKS_FILE_PATH = Path(__file__).parent.parent.joinpath('data', 'books.json')

    def __init__(self, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.books_file = books_file
        self.books = []
        self.load_books()

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            self.save_books()
            return True
        return False

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.save_books()
            return True
        return False

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

    def get_reserved_books(self):
        reserved_books = SearchFilter.filter_reserved_books(self.books)
        return reserved_books

    def get_borrowed_books(self):
        borrowed_books = SearchFilter.filter_borrowed_books(self.books)
        return borrowed_books

    def get_awaiting_to_return_books(self):
        awaiting_to_return_books = SearchFilter.filter_awaiting_to_return_books(self.books)
        return awaiting_to_return_books

    def get_books(self):
        return self.books
