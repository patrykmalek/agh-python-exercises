class Option:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __repr__(self):
        return self.name


class OptionMenu(Option):
    def __init__(self, name, function, submenu=None):
        super().__init__(name, function)
        self.submenu = submenu

    def __repr__(self):
        return self.name
