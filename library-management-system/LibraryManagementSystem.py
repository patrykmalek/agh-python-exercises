from Menu import Menu
from Option import Option, OptionMenu
from Library import Library


class LibraryManagementSystem:

    def __init__(self):
        self.library = Library()
        self.current_menu = None

    def run(self):
        books_management_by_librarian = Menu("Zarządzanie książkami", [
            Option("Wyświetl książki", self.library.display_books),
            Option("Wyszukaj książkę", self.library.search_book),
            Option("Dodaj książkę", self.library.add_book),
            Option("Usuń książkę", self.library.remove_book)
        ])

        readers_management_by_librarian = Menu("Zarządzanie czytelnikami", [
            Option("Wyszukaj czytelnika", self.library.search_reader),
            Option("Dodaj czytelnika", self.library.add_reader),
            Option("Usuń czytelnika", self.library.remove_reader)
        ])

        librarian_main_menu = Menu("Główne menu", [
            Option("Wypożycz książkę", self.library.borrow_book),
            OptionMenu("Zarządzanie książkami", None, books_management_by_librarian),
            OptionMenu("Zarządzanie czytelnikami", None, readers_management_by_librarian),
        ])

        self.current_menu = librarian_main_menu
        self.library.library_management_system = self
        self.current_menu.library_management_system = self
        librarian_main_menu.execute_menu()


"""
URUCHOMIENIE PROGRAMU
"""
library_management_system = LibraryManagementSystem()
library_management_system.run()
