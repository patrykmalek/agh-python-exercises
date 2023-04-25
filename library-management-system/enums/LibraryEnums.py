from enum import Enum
from utils.CommonFunction import CommonFunction


class MenuNames(Enum):
    MAIN_MENU = "Główne menu"
    BOOKS_MANAGEMENT = "Zarządzanie książkami"
    READERS_MANAGEMENT = "Zarządzanie czytelnikami"
    ALL_BOOKS = "Wszystkie książki"
    BORROWED_BOOKS = "Wypożyczone książki"
    RESERVED_BOOKS = "Zarezerwowane książki"
    ADD_BOOK = "Dodawanie książki"
    REMOVE_BOOK = "Usuwanie książki"
    SEARCH_BOOK = "Wyszukiwanie książki"
    BORROW_BOOK = "Wypożyczanie książki"
    ALL_READERS = "Czytelnicy"
    ADD_READER = "Dodawanie czytelnika"
    SEARCH_READER = "Wyszukiwanie czytelnika"
    BACK = "Cofnij"
    EXIT = "Wyjdź"


class Messages(Enum):
    WELCOME = CommonFunction.create_bordered_string("Witaj w bibliotece!", length=100, fill_char=" ") + "\n" + \
              CommonFunction.create_bordered_string("System stworzony do obsługi biblioteki na potrzeby laboratorium "
                                                    "na uczelni AGH", length=100, fill_char=" ") + "\n" + \
              CommonFunction.create_bordered_string("Autor: Patryk Małek", length=100, fill_char=" ") + "\n"
    BOOK_ADDED = "Książka została dodana do biblioteki"
    BOOK_ADDED_ERROR = "Nie powiodło się dodanie książki do biblioteki"
    BOOK_REMOVED = "Książka została usunięta z biblioteki"
    BOOK_REMOVED_ERROR = "Nie powiodło się usunięcie książki z biblioteki"
    BOOK_NOT_FOUND = "Nie znaleziono książki"
    READER_ADDED = "Czytelnik został dodany do biblioteki"
    READER_NOT_FOUND = "Nie znaleziono czytelnika"
    READER_NOT_FOUND_BY_CARD = "Nie znaleziono czytelnika o podanym numerze karty"
    BORROW_SUCCESSFUL = "Książka została wypożyczona"
    RETURN_SUCCESSFUL = "Książka została zwrócona"
    LOGIN_PROMPT = "Podaj login i hasło, aby się zalogować:"
    LOGIN_SUCCESS = CommonFunction.create_bordered_string("Logowanie udane!", length=100, fill_char=" ")
    LOGIN_FAILED = "Nieprawidłowy login lub hasło"
    LOGIN_FAILED_ERROR = "ERROR: Użytkownik nie został poprawnie zalogowany. Wyjście z systemu.."
    LOGIN_ALREADY_EXIST = "Użytkownik o podanym loginie już istnieje"
    NO_DATA = "Brak danych"
    DEFAULT_INPUT_MESSAGE = "Wybierz opcję z menu: "
    WRONG_CHOICE = "Wybrana pozycja nie istnieje. Wybierz ponownie. \n"
    ISBN_INVALID = "ISBN nie spełnia wymagań 13 cyfr. Podaj poprawny ISBN"
    EXIT_MESSAGE = "Dziękujemy za skorzystanie z systemu biblioteki. Do zobaczenia!"
