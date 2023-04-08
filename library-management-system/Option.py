class Option:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def __repr__(self):
        return self.name


class OptionMenu(Option):
    def __init__(self, name, function, submenu=None, parent_menu=None):
        super().__init__(name, function)
        self.submenu = submenu
        self.parent_menu = parent_menu

    def __repr__(self):
        return self.name
