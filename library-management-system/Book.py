class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None
        self.is_reserved = False
        self.reserved_by = None

    def borrow(self, reader):
        if not self.is_borrowed:
            self.borrowed_by = reader
            self.is_borrowed = True
            return True
        return False

    def reserve(self, reader):
        if not self.is_reserved:
            self.reserved_by = reader
            self.is_reserved = True
            return True
        return False

    def to_dict(self):
        return {'title': self.title, 'author': self.author}

    @staticmethod
    def from_dict(book_dict):
        return Book(book_dict['title'], book_dict['author'])

    def __str__(self):
        return f'"{self.title}" - \033[3m{self.author}\033[0m'
