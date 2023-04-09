from Option import Option, OptionMenu
from CommonFunction import CommonFunction
from LibraryEnums import MenuNames, Messages


class Menu:
    def __init__(self, name, menu_options, custom_input_msg=None):
        self.name = name
        self.options = menu_options
        self.parent_menu = None
        self.library_management_system = None
        self.custom_input_msg = custom_input_msg

    def execute_menu(self):
        CommonFunction.clear_view()
        self.library_management_system.current_menu = self
        while True:
            self.display_menu()

            choice = self.get_input()

            if not self.validate_input(choice):
                continue

            if self.parent_menu is not None and int(choice) == 0:
                self.parent_menu.execute_menu()

            CommonFunction.clear_view()
            choice = int(choice) - 1
            if choice in range(0, len(self.options)):
                selected_option = self.options[choice]
                if isinstance(selected_option, OptionMenu):
                    selected_option.submenu.set_parent_menu(self)
                    selected_option.submenu.library_management_system = self.library_management_system
                    selected_option.submenu.execute_menu()
                elif isinstance(selected_option, Option):
                    selected_option.action()
            else:
                print(Messages.WRONG_CHOICE.value)

    def execute_menu_and_get_object(self, filter_func=None):
        self.library_management_system.current_menu = self
        filtered_options = self.options

        while True:
            CommonFunction.clear_view()
            print(len(filtered_options))
            self.display_menu(filtered_options)
            choice_or_query = self.get_input()

            if not choice_or_query:
                filtered_options = self.options
                continue

            if not self.validate_input(choice_or_query, can_be_text=True):
                continue

            if self.parent_menu and choice_or_query.isdigit():
                if int(choice_or_query) == 0:
                    self.parent_menu.execute_menu()

            if choice_or_query.isdigit():
                choice = int(choice_or_query) - 1
                if choice in range(0, len(filtered_options)):
                    selected_option = filtered_options[choice]
                    if isinstance(selected_option, Option):
                        return selected_option.obj_instance

            if filter_func and isinstance(choice_or_query, str):
                query = choice_or_query.lower()
                filtered_options = filter_func(filtered_options, query)

    def display_menu(self, options=None):
        print(CommonFunction.create_bordered_string(self.name))
        print(CommonFunction.create_bordered_string("", fill_char="#"))
        options_to_display = options if options is not None else self.options
        if len(options_to_display) == 0:
            print(f'\n {CommonFunction.create_bordered_string(Messages.NO_DATA.value, fill_char=" ")} \n')
        for index, option in enumerate(options_to_display):
            print(f"{index + 1}. {option}")
        if self.parent_menu:
            print(f"0. {MenuNames.BACK.value}")
        print(f"q. {MenuNames.EXIT.value}")
        print(CommonFunction.create_bordered_string("", fill_char="#"))

    def set_parent_menu(self, parent_menu):
        self.parent_menu = parent_menu

    def get_input(self):
        input_msg = self.custom_input_msg if self.custom_input_msg else Messages.DEFAULT_INPUT_MESSAGE.value
        selected_option = input(input_msg)
        return selected_option

    def validate_input(self, choice, can_be_text=False):
        if choice.lower() == 'q':
            CommonFunction.clear_view()
            print(Messages.EXIT_MESSAGE.value)
            exit()

        if not choice.isdigit() and not can_be_text:
            CommonFunction.clear_view()
            print(Messages.WRONG_CHOICE.value)
            return False

        if not self.parent_menu and int(choice) == 0:
            CommonFunction.clear_view()
            print(Messages.WRONG_CHOICE.value)
            return False

        return True
