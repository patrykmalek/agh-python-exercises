from Reader import Reader
from Librarian import Librarian
from LibraryEnums import Messages
from pathlib import Path
import os
import json


class LoginProvider:
    DEFAULT_USERS_FILE_PATH = Path('data', 'users.json')

    def __init__(self, users_file=DEFAULT_USERS_FILE_PATH):
        self.users_file = users_file
        self.users = []

        self.load_users()

    def load_users(self):
        if not os.path.getsize(self.users_file) == 0:
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def add_user(self, user):
        self.users.append(user.to_dict())
        self.save_users()

    def register_reader(self, library_card_number):
        login, password, first_name, family_name = self.get_input()
        reader = Reader(login, password, first_name, family_name, library_card_number)
        self.add_user(reader)
        return reader

    def register_librarian(self, librarian_id):
        login, password, first_name, family_name = self.get_input()
        librarian = Librarian(login, password, first_name, family_name, librarian_id)
        self.add_user(librarian)
        return librarian

    def get_input(self):
        while True:
            login = input("Login: ")
            if self.validate_login(login):
                break
        password = input("Hasło: ")
        first_name = input("Imię: ")
        family_name = input("Nazwisko: ")
        return login, password, first_name, family_name

    def validate_login(self, login):
        for user_data in self.users:
            if user_data["login"] == login:
                print(Messages.LOGIN_ALREADY_EXIST.value)
                return False
        return True

    def get_user(self, login):
        for user_data in self.users:
            if user_data["login"] == login:
                if user_data['role'] == 'reader':
                    return Reader.from_dict(user_data)
                elif user_data['role'] == 'librarian':
                    return Librarian.from_dict(user_data)
        return None

    def get_readers(self):
        readers_list = []
        for user_data in self.users:
            if user_data['role'] == 'reader':
                readers_list.append(Reader.from_dict(user_data))
        return readers_list

    def get_librarians(self):
        librarians_list = []
        for user_data in self.users:
            if user_data['role'] == 'librarian':
                librarians_list.append(Librarian.from_dict(user_data))
        return librarians_list
