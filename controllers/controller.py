from views.view import View
from models.number import Number


class Controller:
    def __init__(self, view: View, number_type: type[Number]) -> None:
        self.view = view
        self.number_type = number_type

    def run(self) -> None:
        while True:
            command: str = self.view.show_menu()
            if command == "quit":
                return
            user_input: tuple[float, float] = self.view.get_number(
                "Input first number with space between real and imaginary parts: "
            )
            number_one = self.number_type(*user_input)
            user_input: tuple[float, float] = self.view.get_number(
                "Input second number with space between real and imaginary parts: "
            )
            number_two = self.number_type(*user_input)
            if command == "add":
                self.view.show_result(str(number_one + number_two))
            if command == "sub":
                self.view.show_result(str(number_one - number_two))
            if command == "mul":
                self.view.show_result(str(number_one * number_two))
