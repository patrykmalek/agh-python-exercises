class Reader:
    def __init__(self, first_name, family_name, library_card_number):
        self.first_name = first_name
        self.family_name = family_name
        self.borrowed_books = []
        self.reserved_books = []
        self.library_card_number = library_card_number

    def to_dict(self):
        return {'first_name': self.first_name, 'family_name': self.family_name,
                'library_card_number': self.library_card_number}

    @staticmethod
    def from_dict(reader_dict):
        return Reader(reader_dict['first_name'], reader_dict['family_name'], reader_dict['library_card_number'])

    def __str__(self):
        return f"Imię i nazwisko: {self.first_name} {self.family_name}" \
               f"\nNumer karty bibliotecznej: {self.library_card_number}"
