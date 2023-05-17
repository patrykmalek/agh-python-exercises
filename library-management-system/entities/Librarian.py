from enums.UserRole import UserRole

from .User import User


class Librarian(User):
    def __init__(self, user_id, login, password, first_name, family_name, librarian_id):
        super().__init__(user_id, login, password, first_name, family_name, UserRole.LIBRARIAN)
        self.librarian_id = librarian_id

    def to_dict(self):
        librarian_dict = super().to_dict()
        librarian_dict.update({
            'librarian_id': self.librarian_id
        })
        return librarian_dict

    @staticmethod
    def from_dict(librarian_dict):
        return Librarian(
            librarian_dict['user_id'],
            librarian_dict['login'],
            librarian_dict['password'],
            librarian_dict['first_name'],
            librarian_dict['family_name'],
            librarian_dict['librarian_id'])

    def __str__(self):
        return f"Imię i nazwisko: {self.first_name} {self.family_name}" \
               f"\nIdentyfikator bibliotekarza: {self.library_card_number}"
