from entities.Menu import Menu
from entities.Option import Option, OptionMenu
from enums.LibraryEnums import MenuNames, Messages
from services.Library import Library
from services.LoginProvider import LoginProvider
from utils.CommonFunction import CommonFunction
from repositories.UserRepository import UserRepository
import time


class LibraryManagementSystem:

    def __init__(self):
        self.user_repository = UserRepository()
        self.login_provider = LoginProvider(self.user_repository)
        self.library = Library(self.login_provider, self.user_repository)
        self.current_menu = None

    def run(self):
        books_management_by_librarian = Menu(MenuNames.BOOKS_MANAGEMENT.value, [
            Option("Wyświetl książki", self.library.display_books),
            Option("Wyświetl wypożyczone książki", self.library.display_borrowed_books),
            Option("Wyświetl zarezerwowane książki", self.library.display_reserved_books),
            Option("Wyszukaj książkę", self.library.search_book),
            Option("Dodaj książkę", self.library.add_book),
            Option("Usuń książkę", self.library.remove_book)
        ])

        readers_management_by_librarian = Menu(MenuNames.READERS_MANAGEMENT.value, [
            Option("Wyświetl czytelników", self.library.display_readers),
            Option("Wyszukaj czytelnika", self.library.search_reader),
            Option("Dodaj czytelnika", self.library.add_reader),
        ])

        librarian_main_menu = Menu(MenuNames.MAIN_MENU.value, [
            Option("Wypożycz książkę", self.library.borrow_book),
            OptionMenu("Zarządzanie książkami", None, books_management_by_librarian),
            OptionMenu("Zarządzanie czytelnikami", None, readers_management_by_librarian),
        ])

        self.current_menu = librarian_main_menu
        self.library.library_management_system = self
        self.current_menu.library_management_system = self

        CommonFunction.clear_view()
        print(Messages.WELCOME.value)
        time.sleep(3)

        librarian_main_menu.execute_menu()


"""
URUCHOMIENIE PROGRAMU
"""
library_management_system = LibraryManagementSystem()
library_management_system.run()
