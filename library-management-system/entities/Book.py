

class Book:

    def __init__(self, isbn, title, author, is_borrowed=False, borrowed_by=None,
                 is_reserved=False, reserved_by=None, to_return=False):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by  # in json stored as id of reader
        self.is_reserved = is_reserved
        self.reserved_by = reserved_by  # in json stored as id of reader
        self.to_return = to_return

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

    def marked_for_return(self, reader):
        if self.is_borrowed and self.borrowed_by.user_id == reader.user_id:
            self.to_return = True
            return True
        return False

    @staticmethod
    def validate_isbn(isbn):
        if len(isbn) == 13:
            return True
        return False

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'is_borrowed': self.is_borrowed,
            'borrowed_by': self.borrowed_by.user_id if self.borrowed_by else None,
            'is_reserved': self.is_reserved,
            'reserved_by': self.reserved_by.user_id if self.reserved_by else None,
            'to_return': self.to_return
        }

    @staticmethod
    def from_dict(book_dict):
        return Book(
            book_dict['isbn'],
            book_dict['title'],
            book_dict['author'],
            book_dict['is_borrowed'],
            book_dict["borrowed_by"],
            book_dict['is_reserved'],
            book_dict["reserved_by"],
            book_dict['to_return']
        )

    def __str__(self):
        return f'({self.isbn}) "{self.title}" - \033[3m{self.author}\033[0m'
