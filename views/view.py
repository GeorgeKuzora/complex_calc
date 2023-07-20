from typing import Protocol


class View(Protocol):

    def get_number(self, message: str) -> tuple[float, float]: ...

    def show_menu(self) -> str: ...

    def show_result(self, result: str) -> None: ...
