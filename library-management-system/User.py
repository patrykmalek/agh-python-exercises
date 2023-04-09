class User:
    def __init__(self, login, password, first_name, family_name, role):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.family_name = family_name
        self.role = role

    def to_dict(self):
        return {
            'login': self.login,
            'password': self.password,
            'first_name': self.first_name,
            'family_name': self.family_name,
            'role': self.role
        }
