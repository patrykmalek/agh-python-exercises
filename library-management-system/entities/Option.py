class Option:
    def __init__(self, name, action=None, obj_instance=None):
        self.name = name
        self.action = action
        self.obj_instance = obj_instance  # ??

    def __repr__(self):
        return self.name


class OptionMenu(Option):  # MenuOption?
    def __init__(self, name, function, submenu=None):
        super().__init__(name, function)
        self.submenu = submenu

    def __repr__(self):
        return self.name
