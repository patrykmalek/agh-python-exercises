from entities.Reader import Reader
from entities.Librarian import Librarian
from enums.LibraryEnums import Messages
from utils.CommonFunction import CommonFunction


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

    def login(self):
        print(Messages.LOGIN_PROMPT.value)
        while True:
            login, password = self.get_login_prompt()
            user = self.user_repository.get_user_by_login(login)
            CommonFunction.clear_view()
            print(Messages.WELCOME.value)
            if user and user.password == password:
                print(Messages.LOGIN_SUCCESS.value)
                return user
            else:
                print(Messages.LOGIN_FAILED.value)

    @staticmethod
    def get_login_prompt():
        login = input("Login: ")
        password = input("Hasło: ")
        return login, password
