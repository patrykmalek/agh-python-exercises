from enum import Enum
from CommonFunction import CommonFunction


class MenuNames(Enum):
    MAIN_MENU = "Główne menu"
    BOOKS_MANAGEMENT = "Zarządzanie książkami"
    READERS_MANAGEMENT = "Zarządzanie czytelnikami"
    ALL_BOOKS = "Wszystkie książki"
    BORROWED_BOOKS = "Wypożyczone książki"
    RESERVED_BOOKS = "Zarezerwowane książki"
    ADD_BOOK = "Dodawanie książki"
    REMOVE_BOOK = "Usuwanie książki"
    ADD_READER = "Dodawanie czytelnika"


class Messages(Enum):
    WELCOME = CommonFunction.create_bordered_string("Witaj w bibliotece!", length=100, fill_char=" ") + "\n" + \
              CommonFunction.create_bordered_string("System stworzony do obsługi biblioteki na potrzeby laboratorium "
                                                    "na uczelni AGH", length=100, fill_char=" ") + "\n" + \
              CommonFunction.create_bordered_string("Autor: Patryk Małek", length=100, fill_char=" ")
    BOOK_ADDED = "Książka została dodana do biblioteki"
    BOOK_REMOVED = "Książka została usunięta z biblioteki"
    BOOK_NOT_FOUND = "Nie znaleziono książki"
    READER_ADDED = "Czytelnik został dodany do biblioteki"
    READER_NOT_FOUND = "Nie znaleziono czytelnika"
    READER_NOT_FOUND_BY_CARD = "Nie znaleziono czytelnika o podanym numerze karty"
    BORROW_SUCCESSFUL = "Książka została wypożyczona"
    RETURN_SUCCESSFUL = "Książka została zwrócona"
    LOGIN_FAILED = "Nieprawidłowy login lub hasło"
    LOGIN_ALREADY_EXIST = "Użytkownik o podanym loginie już istnieje"
    NO_DATA = "Brak danych"
