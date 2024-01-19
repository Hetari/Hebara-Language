from typing import Any


class Tokens:
    def __init__(self, type: str, value: Any) -> None:
        """
        Initializes an instance of the class.

        Args:
            type (str): The type of the instance.
            value (Any): The value of the instance.
        """
        self.type = type
        self.value = value

    def __repr__(self):
        """
        Return a string representation of the value stored in the object.
        """
        return str(self.value)


class Integer(Tokens):
    def __init__(self, value: int):
        super().__init__("INTEGER", value)


class String(Tokens):
    def __init__(self, value: str):
        super().__init__("STRING", value)


class Boolean(Tokens):
    def __init__(self, value: bool):
        super().__init__("BOOLEAN", value)


class Float(Tokens):
    def __init__(self, value: float):
        super().__init__("FLOAT", value)


class Operations(Tokens):
    def __init__(self, value: str):
        super().__init__("OP", value)
