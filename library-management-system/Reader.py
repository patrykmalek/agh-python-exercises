from User import User


class Reader(User):
    def __init__(self, user_id, login, password, first_name, family_name,
                 library_card_number, borrowed_books=[], reserved_books=[]):
        super().__init__(user_id, login, password, first_name, family_name, 'reader')
        self.library_card_number = library_card_number
        self.borrowed_books = borrowed_books
        self.reserved_books = reserved_books

    def to_dict(self):
        reader_dict = super().to_dict()
        reader_dict.update({
            'library_card_number': self.library_card_number,
            'borrowed_books': self.borrowed_books,
            'reserved_books': self.reserved_books
        })
        return reader_dict

    @staticmethod
    def from_dict(reader_dict):
        return Reader(
            reader_dict['user_id'],
            reader_dict['login'],
            reader_dict['password'],
            reader_dict['first_name'],
            reader_dict['family_name'],
            reader_dict['library_card_number'],
            reader_dict['borrowed_books'],
            reader_dict['reserved_books'])

    def __str__(self):
        return f"Imię i nazwisko: {self.first_name} {self.family_name}" \
               f"\nNumer karty bibliotecznej: {self.library_card_number}"

    def to_string(self):
        return f"{self.library_card_number} - {self.first_name} {self.family_name} ({self.login})"  \
               f"\n    Książki:\n     -wypożyczone: {len(self.borrowed_books)}\n     " \
               f"-zarezerwowane: {len(self.reserved_books)}"
