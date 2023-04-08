from Book import Book


class Library:

    def __init__(self, books_file="books.csv", readers_file="readers.csv"):
        self.books = []
        self.borrowed_books = []
        self.reserved_book = []
        self.readers = []
        self.books_file = books_file
        self.readers_file = readers_file

        # Load library state from CSV files or json?
        self.load_books()
        self.load_readers()

    def display_books(self):
        print(f"\n--------- Wyświetlanie książek ---------")
        if len(self.books) == 0:
            print("      Brak danych...      ")
        for index, book in enumerate(self.books):
            print(f'{index + 1}.  "{book.title}" - \033[3m{book.author}\033[0m')
    def search_book(self):
        print("Searching book...")

    def add_book(self):
        print(f"\n--------- Dodawanie książki ---------")
        title = input("Podaj tytuł:")
        author = input("Podaj autora:")

        book = Book(title, author)
        self.books.append(book)
        print(f"Dodano książkę: {book}")

    def remove_book(self):
        print("Removing book...")

    def borrow_book(self):
        print("Borrowing book...")

    def return_book(self):
        print("Returning book...")

    def search_reader(self):
        print("Searching reader...")

    def add_reader(self):
        print("Adding reader...")

    def remove_reader(self):
        print("Removing reader...")

    def load_books(self):
        # TODO: Add loading data from CSV or JSON file.
        pass

    def load_readers(self):
        # TODO: Add loading data from CSV or JSON file.
        pass
