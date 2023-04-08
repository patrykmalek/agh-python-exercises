from Option import Option, OptionMenu
import os


class Menu:
    def __init__(self, name, menu_options):
        self.name = name
        self.options = menu_options
        self.parent_menu = None
        self.clear_view()

    def execute_menu(self):
        self.clear_view()
        while True:
            self.display_menu()

            choice = self.get_input()

            if not self.validate_input(choice):
                continue

            if self.parent_menu is not None and int(choice) == 0:
                self.parent_menu.execute_menu()

            self.clear_view()
            choice = int(choice) - 1
            if choice in range(0, len(self.options)):
                selected_option = self.options[choice]
                if isinstance(selected_option, OptionMenu):
                    selected_option.submenu.set_parent_menu(self)
                    selected_option.submenu.execute_menu()
                elif isinstance(selected_option, Option):
                    selected_option.action()
            else:
                print("Coś poszło nie tak...")

    def display_menu(self):
        print(f"\n--------- {self.name} ---------")
        print("#############################")
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")
        if self.parent_menu is not None:
            print(f"0. Back")
        print("q. Exit")
        print("#############################")

    def set_parent_menu(self, parent_menu):
        self.parent_menu = parent_menu

    def get_input(self):
        selected_option = input("Select an option: ")
        return selected_option

    def validate_input(self, choice):
        if choice.lower() == 'q':
            self.clear_view()
            print("Wyjście z programu...")
            exit()

        if not choice.isdigit():
            self.clear_view()
            print("Niepoprawna opcja...")
            return False

        if self.parent_menu is None and int(choice) == 0:
            self.clear_view()
            print("Niepoprawna opcja...")
            return False

        return True

    def clear_view(self):
        os.system('cls' if os.name == 'nt' else 'clear')
