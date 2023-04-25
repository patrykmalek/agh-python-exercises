import uuid


class User:
    def __init__(self, user_id, login, password, first_name, family_name, role):
        self.user_id = user_id if user_id else str(uuid.uuid4())
        self.login = login
        self.password = password
        self.first_name = first_name
        self.family_name = family_name
        self.role = role

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'password': self.password,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'role': self.role
        }
