from Option import Option, OptionMenu


class Menu:
    def __init__(self, menu_options, parent_menu=None):
        self.options = menu_options
        self.parent_menu = parent_menu
        self.current_menu = menu_options
        self.menu_history = []

    def display_menu(self):
        print("##############################")
        for index, option in enumerate(self.current_menu):
            print(f"{index + 1}. {option}")
        if self.parent_menu is not None:
            print(f"0. Back")
        print("q. Exit")
        print("##############################")

    def get_input(self):
        selected_option = input("Select an option: ")
        return selected_option

    def validate_input(self, choice):
        if choice.lower() == 'q':
            print("Wyjście z programu...")
            exit()

        if not choice.isdigit():
            print("Niepoprawna opcja...")
            return False

        if self.parent_menu is None and int(choice) == 0:
            print("Niepoprawna opcja...")
            return False

        return True

    def execute_menu(self):
        while True:
            self.display_menu()

            choice = self.get_input()

            if not self.validate_input(choice):
                continue

            choice = int(choice)
            if choice in range(0, len(self.options) + 1):
                selected_option = self.options[choice - 1]

                print(f"Wybrano opcję: {selected_option}")
                return selected_option
            else:
                print("Coś poszło nie tak...")


# testowe uzycie funkcji

def function1():
    print("You chose function 1.")


def function2():
    print("You chose function 2.")


main_options = [
    Option("Function 1", function1),
    Option("Function 2", function2),
]

menu = Menu(main_options)

menu.execute_menu()
