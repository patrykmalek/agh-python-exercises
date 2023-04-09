from Reader import Reader
from Librarian import Librarian
from pathlib import Path
import os
import json


class LoginProvider:
    DEFAULT_USERS_FILE_PATH = Path('data', 'users.json')

    def __init__(self, users_file=DEFAULT_USERS_FILE_PATH):
        self.users_file = users_file
        self.users = {}

    def load_users(self):
        if not os.path.getsize(self.users_file) == 0:
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def add_user(self, user):
        self.users[user.login] = user.to_dict()
        self.save_users()

    def get_user(self, login):
        if login in self.users:
            user_data = self.users[login]
            if user_data['role'] == 'reader':
                return Reader.from_dict(user_data)
            elif user_data['role'] == 'librarian':
                return Librarian.from_dict(user_data)
        return None
