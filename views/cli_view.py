from log_config import logging


class ViewCLI:

    AVALIABLE_COMMANDS = ["add", "sub", "mul", "quit"]

    def get_number(self, message: str) -> tuple[float, float]:
        try:
            numbers = input(message).split()
            return float(numbers[0]), float(numbers[1])
        except (ValueError, IndexError) as e:
            logging.exception(msg="wrong user number input")
            print(f"Incorect input value caused error: {e}")
            return self.get_number(message)

    def show_menu(self) -> str:
        print("Input one of the following commands")
        print("add - for addition")
        print("sub - for substraction")
        print("mul - for multiplication")
        print("quit - for quit")
        command = input("Your command: ").lower()
        if (command in self.AVALIABLE_COMMANDS):
            return command
        logging.error(msg="wrong user command input")
        print("Incorect input value caused error")
        return self.show_menu()

    def show_result(self, result: str) -> None:
        print(f"Result is: {result}")
