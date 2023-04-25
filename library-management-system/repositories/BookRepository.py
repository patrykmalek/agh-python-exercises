from pathlib import Path


class BookRepository:
    DEFAULT_BOOKS_FILE_PATH = Path('../data', 'books.json')
    
    def __init__(self, books_file=DEFAULT_BOOKS_FILE_PATH):
        self.books_file = books_file