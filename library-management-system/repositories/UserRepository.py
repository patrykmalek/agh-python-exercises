from pathlib import Path
from entities.Reader import Reader
from entities.Librarian import Librarian
from enums.UserRole import UserRole
import os
import json


class UserRepository:
    DEFAULT_USERS_FILE_PATH = Path(__file__).parent.parent.joinpath('data', 'users.json')

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
        self.readers.append(user)
        self.librarians.append(user)
        self.save_users()

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

    def get_user_by_login(self, login):
        for user_data in self.users:
            if user_data["login"] == login:
                if user_data['role'] == UserRole.READER.value:
                    return Reader.from_dict(user_data)
                elif user_data['role'] == UserRole.LIBRARIAN.value:
                    return Librarian.from_dict(user_data)
        return None

    def get_reader_by_id(self, reader_id):
        readers_dict = {reader.user_id: reader for reader in self.readers}
        return readers_dict.get(reader_id)
