import json
import os
from pathlib import Path

from entities.Librarian import Librarian
from entities.Reader import Reader
from enums.UserRole import UserRole


class UserRepository:
    DEFAULT_USERS_FILE_PATH = Path(__file__).parent.parent.joinpath('data', 'users.json')
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, users_file=DEFAULT_USERS_FILE_PATH):
        self.users_file = users_file
        self.users = []
        self.readers = []
        self.librarians = []
        self.load_users()
        self.load_readers()
        self.load_librarians()

    def add_user(self, user):
        self.users.append(user.to_dict())
        if user.role == UserRole.READER:
            self.readers.append(user)
        if user.role == UserRole.LIBRARIAN:
            self.librarians.append(user)
        self.save_users()

    def update_user(self, updated_user):
        updated_user_dict = updated_user.to_dict()
        for user_data in self.users:
            if user_data['user_id'] == updated_user_dict['user_id']:
                user_data['login'] = updated_user_dict['login']
                user_data['password'] = updated_user_dict['password']  # TODO: maybe hashed password?
                user_data['first_name'] = updated_user_dict['first_name']
                user_data['family_name'] = updated_user_dict['family_name']
                if user_data['role'] == UserRole.READER.value:
                    user_data['library_card_number'] = updated_user_dict['library_card_number']
                    user_data['borrowed_books'] = updated_user_dict['borrowed_books']
                    user_data['reserved_books'] = updated_user_dict['reserved_books']
                if user_data['role'] == UserRole.LIBRARIAN.value:
                    user_data['librarian_id'] = updated_user_dict['librarian_id']
                self.save_users()
                return True
        return False

    def load_users(self):
        if not os.path.getsize(self.users_file) == 0:
            with open(self.users_file, 'r', encoding='utf-8') as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f)

    def load_readers(self):
        for user_data in self.users:
            if user_data['role'] == 'reader':
                self.readers.append(Reader.from_dict(user_data))

    def load_librarians(self):
        for user_data in self.users:
            if user_data['role'] == 'librarian':
                self.librarians.append(Librarian.from_dict(user_data))

    def add_links_to_book(self, book_repository):
        for reader in self.readers:
            borrowed_books = reader.borrowed_books
            reserved_books = reader.reserved_books
            reader.borrowed_books = []
            reader.reserved_books = []
            for book_isbn in borrowed_books:
                book = book_repository.get_book_by_isbn(book_isbn)
                if book:
                    reader.borrowed_books.append(book)
            for book_isbn in reserved_books:
                book = book_repository.get_book_by_isbn(book_isbn)
                if book:
                    reader.reserved_books.append(book)

    def get_user_by_login(self, login):
        readers_dict = {reader.login: reader for reader in self.readers}
        librarians_dict = {librarian.login: librarian for librarian in self.librarians}
        if login in readers_dict:
            return readers_dict.get(login)
        if login in librarians_dict:
            return librarians_dict.get(login)
        return None

    def get_reader_by_id(self, reader_id):
        readers_dict = {reader.user_id: reader for reader in self.readers}
        return readers_dict.get(reader_id)
