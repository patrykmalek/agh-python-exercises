import datetime


class Book:

    def __init__(self, isbn, title, author, is_borrowed=False, borrowed_by=None,
                 is_reserved=False, reserved_by=None, to_return=False, due_borrow_date=None, due_reservation_date=None):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by  # in json stored as id of reader
        self.is_reserved = is_reserved
        self.reserved_by = reserved_by  # in json stored as id of reader
        self.to_return = to_return
        self.due_borrow_date = due_borrow_date
        self.due_reservation_date = due_reservation_date

    def borrow(self, reader):
        if self.is_borrowed:
            return False
        elif self.is_reserved and self.reserved_by.user_id != reader.user_id:
            return False
        else:
            self.borrowed_by = reader
            self.is_borrowed = True
            self.due_borrow_date = datetime.date.today() + datetime.timedelta(days=30)
            if self.is_reserved:
                self.reserved_by = None
                self.is_reserved = False
                self.due_borrow_date = None
                self.due_reservation_date = None
            return True

    def extend_due_borrow_date(self, reader):
        if self.due_borrow_date < datetime.date.today() or self.is_reserved or \
                not self.is_borrowed or (self.is_borrowed and self.borrowed_by.user_id != reader.user_id):
            return False
        self.due_borrow_date += datetime.timedelta(days=7)
        return True

    def reserve(self, reader):
        if not self.is_reserved:
            self.reserved_by = reader
            self.is_reserved = True
            self.due_reservation_date = datetime.date.today() + datetime.timedelta(days=7)
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
            'to_return': self.to_return,
            'due_borrow_date': self.due_borrow_date.strftime('%Y-%m-%d') if self.due_borrow_date else None,
            'due_reservation_date': self.due_reservation_date.strftime('%Y-%m-%d') if self.due_reservation_date else None
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
            book_dict['to_return'],
            datetime.datetime.strptime(book_dict['due_borrow_date'], '%Y-%m-%d').date()
            if book_dict['due_borrow_date'] else None,
            datetime.datetime.strptime(book_dict['due_reservation_date'], '%Y-%m-%d').date()
            if book_dict['due_reservation_date'] else None
        )

    def __str__(self):
        return f'({self.isbn}) "{self.title}" - \033[3m{self.author}\033[0m'
