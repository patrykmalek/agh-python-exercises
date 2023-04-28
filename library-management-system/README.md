# 📚 Projekt Systemu do obsługi biblioteki

## Wymagania:

System ma być obsługiwany przez konsolę, a tam, gdzie to możliwe, powinno być dostępne konsolowe, interaktywne menu.

- Możliwość logowania jako czytelnik lub bibliotekarz.
- Czytelnik powinien mieć możliwość wypożyczenia książki, zarezerwowania wypożyczonej książki, przedłużenia wypożyczenia oraz przeglądania katalogu (wyszukiwanie po tytule, autorze lub słowach kluczowych).
- Bibliotekarz powinien mieć możliwość przyjęcia zwrotu książki, dodania nowej książki, usunięcia książki z systemu, dodania czytelnika.
- System powinien przechowywać swoje dane na dysku — zmiany dokonane podczas jednego uruchomienia programu mają być widoczne w kolejnych.

## Wymagane funkcje

Poniżej znajduje się lista funkcji, które powinny być dostępne w systemie:

### Dla czytelnika:

- Logowanie do systemu jako czytelnik ✔
- Przeglądanie katalogu książek ✔
- Wyszukiwanie książek po tytule, autorze lub słowach kluczowych ✔
- Wypożyczanie książek ✔
- Zwracanie książek ✔
- Przedłużanie wypożyczenia książek ✔
- Rezerwowanie już wypożyczonych książek przez innego czytelnika ✔

### Dla bibliotekarza:

- Logowanie do systemu jako bibliotekarz ✔
- Przeglądanie katalogu książek ✔
- Dodawanie nowych książek do katalogu ✔
- Przyjmowanie zwrotów książek ✔
- Usuwanie książek z katalogu ✔
- Dodawanie nowych czytelników do systemu ✔

## Przechowywanie danych

Dane powinny być przechowywane w plikach tekstowych na dysku w strukturze, która umożliwi łatwe wyszukiwanie, dodawanie i usuwanie danych.
np. pliki tekstowe, CSV lub JSON

## Uruchamianie systemu

#### Wersja interpretera:

- 🐍 Python 3.10

#### Polecenie:

Aby uruchomić system należy sklonować repozytorium z kodem źródłowym, 
przejść do katalogu z projektem i uruchomić projekt poleceniem `python LibraryManagmentSystem.py`
