from pathlib import Path
from entities.Book import Book
from utils.SearchFilter import SearchFilter
import os
import json
from repositories.UserRepository import UserRepository


class BookRepository:
    DEFAULT_BOOKS_FILE_PATH = Path(__file__).parent.parent.joinpath('data', 'books.json')
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.books_file = books_file
        self.books = []
        self.load_books()

    def add_book(self, book):
        isbn_books = [book.isbn for book in self.books]
        if book.isbn not in isbn_books:
            self.books.append(book)
            self.save_books()
            return True
        return False

    def remove_book(self, book):
        isbn_books = [book.isbn for book in self.books]
        if book.isbn in isbn_books:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def update_book(self, updated_book):
        for book in self.books:
            if book.isbn == updated_book.isbn:
                book.title = updated_book.title
                book.author = updated_book.author
                book.is_borrowed = updated_book.is_borrowed
                book.borrowed_by = updated_book.borrowed_by
                book.is_reserved = updated_book.is_reserved
                book.reserved_by = updated_book.reserved_by
                book.to_return = updated_book.to_return
        self.save_books()

    def load_books(self):
        user_repository = UserRepository()
        if not os.path.getsize(self.books_file) == 0:
            with open(self.books_file, 'r', encoding='utf-8') as file:
                books_dict_list = json.load(file)
            for book_dict in books_dict_list:
                book = Book.from_dict(book_dict)
                borrowed_by = None
                reserved_by = None
                borrowed_by_id = book_dict.get("borrowed_by")
                if borrowed_by_id is not None:
                    borrowed_by = user_repository.get_reader_by_id(borrowed_by_id)
                reserved_by_id = book_dict.get("reserved_by")
                if reserved_by_id is not None:
                    reserved_by = user_repository.get_reader_by_id(reserved_by_id)
                book.borrowed_by = borrowed_by
                book.reserved_by = reserved_by
                self.books.append(book)

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

    def get_book_by_isbn(self, book_isbn):
        books_dict = {book.isbn: book for book in self.books}
        return books_dict.get(book_isbn)
