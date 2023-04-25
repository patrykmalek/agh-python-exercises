from entities.Reader import Reader
from entities.Librarian import Librarian
from enums.LibraryEnums import Messages


class LoginProvider:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_reader(self, library_card_number):
        login, password, first_name, family_name = self.get_input()
        reader = Reader(None, login, password, first_name, family_name, library_card_number)
        self.user_repository.add_user(reader)
        return reader

    def register_librarian(self, librarian_id):
        login, password, first_name, family_name = self.get_input()
        librarian = Librarian(None, login, password, first_name, family_name, librarian_id)
        self.user_repository.add_user(librarian)
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
        for user_data in self.user_repository.users:
            if user_data["login"] == login:
                print(Messages.LOGIN_ALREADY_EXIST.value)
                return False
        return True
