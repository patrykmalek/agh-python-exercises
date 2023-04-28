from enum import Enum
from utils.CommonFunction import CommonFunction


class MenuNames(Enum):
    MAIN_MENU = "Główne menu"
    BOOKS_MANAGEMENT = "Zarządzanie książkami"
    READERS_MANAGEMENT = "Zarządzanie czytelnikami"
    ALL_BOOKS = "Wszystkie książki"
    BORROWED_BOOKS = "Wypożyczone książki"
    RESERVED_BOOKS = "Zarezerwowane książki"
    READER_BORROWED_BOOKS = "Twoje wypożyczone książki"
    READER_RESERVED_BOOKS = "Twoje zarezerwowane książki"
    READER_RETURN_MARK_BOOKS = "Twoje książki do zwrotu"
    ADD_BOOK = "Dodawanie książki"
    REMOVE_BOOK = "Usuwanie książki"
    RETURN_BOOK = "Zwrot książki"
    SEARCH_BOOK = "Wyszukiwanie książki"
    BORROW_BOOK = "Wypożyczanie książki"
    EXTEND_DUE_BORROW_DATE_BOOK = "Przedłużanie wypożyczenia książki"
    CHOOSE_BOOK = "Wybierz książkę (wyszukaj):"
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
    BORROW_SUCCESSFUL = "Książka została wypożyczona. Termin zwrotu:"
    RESERVATION_SUCCESSFUL = "Książka została zarezerwowana do:"
    RETURN_SUCCESSFUL = "Książka została zwrócona"
    BOOK_ALREADY_BORROWED_BY_SM_EL = "Książka jest wypożyczona przez innego użytkownika"
    BOOK_ALREADY_BORROWED_BY_USER = "Książka jest już w Twoim posiadaniu, nie można jej wypożyczyć."
    BOOK_ALREADY_RESERVED_BY_SM_EL = "Książka jest zarezerwowana przez innego użytkownika"
    BOOK_RESERVE_CONFIRM = "Czy zarezerwować dla Ciebie tę książkę? (Y/N): "
    BOOK_BORROW_CONFIRM = "Czy na pewno chcesz wypożyczyć tę książkę? (Y/N): "
    BOOK_EXTEND_DUE_BORROW_DATE_CONFIRM = "Czy na pewno chcesz wydłużyć wypożyczenie tej książki o 7 dni? (Y/N): "
    BOOK_AFTER_EXTEND_DUE_BORROW_DATE_INFO = "Wypożyczenie zostało wydłużone o 7 dni. Nowy termin zwrotu:"
    BOOK_RETURN_CONFIRM = "Czy na pewno chcesz zwrócić tę książkę? (Y/N): "
    BOOK_AFTER_RETURN_INFO = "Książka została oznaczona do zwrotu, " \
                             "proszę udać się do biblioteki w celu fizycznego zwrotu książki."
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
