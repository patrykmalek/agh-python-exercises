from Menu import Menu
from Option import Option, OptionMenu
from Library import Library

library = Library()

book_management = Menu("Zarządzanie książkami", [
    Option("Dodaj książkę", library.add_book),
    Option("Usuń książkę", library.remove_book)
])

main_menu = Menu("Główne menu", [
    Option("Wypożycz książkę", library.borrow_book),
    Option("Zwróć książkę", library.return_book),
    OptionMenu("Zarządzanie książkami", None,  book_management),
])

main_menu.execute_menu()
