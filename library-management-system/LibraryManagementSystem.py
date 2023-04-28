from entities.Menu import Menu
from entities.Option import Option, OptionMenu
from enums.LibraryEnums import MenuNames, Messages
from enums.UserRole import UserRole
from services.Library import Library
from services.LoginProvider import LoginProvider
from services.Session import Session
from utils.CommonFunction import CommonFunction
from repositories.UserRepository import UserRepository
from repositories.BookRepository import BookRepository
import time


class LibraryManagementSystem:

    def __init__(self):
        self.user_repository = UserRepository()
        self.book_repository = BookRepository()
        self.login_provider = LoginProvider(self.user_repository)
        self.library = Library(self.login_provider, self.book_repository, self.user_repository)
        self.session = Session()
        self.current_menu = None

    def run(self):
        CommonFunction.clear_view()
        print(Messages.WELCOME.value)
        user = self.login_provider.login()
        if user:
            self.session.login(user)
            if self.session.current_user.role == UserRole.LIBRARIAN:
                self.current_menu = self.create_librarian_menu()
            if self.session.current_user.role == UserRole.READER:
                self.current_menu = self.create_reader_menu()
            self.library.library_management_system = self
            self.current_menu.library_management_system = self
            time.sleep(3)
            self.current_menu.execute_menu()
        else:
            CommonFunction.clear_view()
            print(Messages.LOGIN_FAILED_ERROR.value)
            exit()

    def create_librarian_menu(self):
        books_management_by_librarian = Menu(MenuNames.BOOKS_MANAGEMENT.value, [
            Option("Wyświetl książki", self.library.display_books),
            Option("Wyświetl wypożyczone książki", self.library.display_borrowed_books),
            Option("Wyświetl zarezerwowane książki", self.library.display_reserved_books),
            Option("Wyszukaj książkę", self.library.search_book),
            Option("Dodaj książkę", self.library.add_book),
            Option("Przyjmij zwrot książki", self.library.accept_return_book),
            Option("Usuń książkę", self.library.remove_book)
        ])

        readers_management_by_librarian = Menu(MenuNames.READERS_MANAGEMENT.value, [
            Option("Wyświetl czytelników", self.library.display_readers),
            Option("Wyszukaj czytelnika", self.library.search_reader),
            Option("Dodaj czytelnika", self.library.add_reader),
        ])

        settings_management = Menu(MenuNames.READERS_MANAGEMENT.value, [
            Option("Zmień hasło", None)
        ])

        librarian_main_menu = Menu(MenuNames.MAIN_MENU.value, [
            OptionMenu("Zarządzanie książkami", None, books_management_by_librarian),
            OptionMenu("Zarządzanie czytelnikami", None, readers_management_by_librarian),
            OptionMenu("Ustawienia konta", None, settings_management),
        ])

        return librarian_main_menu

    def create_reader_menu(self):
        books_management = Menu(MenuNames.BOOKS_MANAGEMENT.value, [
            Option("Wyświetl książki", self.library.display_books),
            Option("Wyświetl wypożyczone książki", self.library.display_reader_borrowed_books),
            Option("Wyświetl zarezerwowane książki", self.library.display_reader_reserved_books),
            Option("Wyświetl książki do zwrotu", self.library.display_reader_with_return_mark_books),
            Option("Wyszukaj książkę", self.library.search_book),
            Option("Wypożycz książkę", self.library.borrow_book),
            Option("Zwróć książkę", self.library.return_book),
            Option("Przedłuż wypożyczenie książki", self.library.extend_due_borrow_date),
        ])

        settings_management = Menu(MenuNames.READERS_MANAGEMENT.value, [
            Option("Zmień hasło", None)
        ])

        reader_main_menu = Menu(MenuNames.MAIN_MENU.value, [
            OptionMenu("Biblioteka", None, books_management),
            OptionMenu("Ustawienia konta", None, settings_management),
        ])

        return reader_main_menu

"""
URUCHOMIENIE PROGRAMU
"""
library_management_system = LibraryManagementSystem()
library_management_system.run()
