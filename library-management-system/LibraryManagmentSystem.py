from Menu import Menu
from Option import Option, OptionMenu
from Library import Library

library = Library()

books_management_by_librarian = Menu("Zarządzanie książkami", [
    Option("Wyświetl książki", library.display_books),
    Option("Wyszukaj książkę", library.search_book),
    Option("Dodaj książkę", library.add_book),
    Option("Usuń książkę", library.remove_book)
])

readers_management_by_librarian = Menu("Zarządzanie czytelnikami", [
    Option("Wyszukaj czytelnika", library.search_reader),
    Option("Dodaj czytelnika", library.add_reader),
    Option("Usuń czytelnika", library.remove_reader)
])

librarian_main_menu = Menu("Główne menu", [
    Option("Wypożycz książkę", library.borrow_book),
    OptionMenu("Zarządzanie książkami", None,  books_management_by_librarian),
    OptionMenu("Zarządzanie czytelnikami", None,  readers_management_by_librarian),
])

librarian_main_menu.execute_menu()
