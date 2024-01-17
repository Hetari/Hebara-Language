import Tokens


class Lexer:
    digits = "0123456789"
    operations = "+-/*()"
    ignore = ["#", "//", " "]

    def __init__(self, text):
        """
        Initializes the class object with the given `text` parameter.

        Parameters:
            text (str): The user input text.

        Returns:
            None
        """
        self.text: str = text
        self.position: int = 0
        self.tokens: list[Tokens.Tokens] = []
        self.char: str = self.text[self.position]
        self.token: Tokens.Tokens = None

    def tokenize(self):
        """
        Tokenize the given text and returns a list of tokens.
        This function iterates through each character in the text and checks if it is a digit, an operation, or an ignored character.
        If it is an ignored character, it continues to the next character without creating a token.
        If it is a digit, it extracts the number as a token.
        If it is an operation, it creates an Operations object as a token.
        After processing all the characters, it returns the list of tokens.
        """
        while self.position < len(self.text):
            if self.char in Lexer.ignore:
                self.move()
                continue

            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Tokens.Operations(self.char)
                self.move()

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self):
        """
        Extracts a number from the input text.

        Returns:
            Tokens.Integer: If the extracted number is an integer.
            Tokens.Float: If the extracted number is a float.
        """
        number = ""
        isFloat = False

        # Iterate through the input text until we reach the end or a non-digit/non-decimal character
        while self.position < len(self.text) and (self.char in Lexer.digits or self.char == "."):
            if self.char == ".":
                isFloat = True

            # Append the current character to the number string
            number += self.char

            # Move to the next character
            self.move()

        # Return an instance of Tokens.Integer if the extracted number is an integer,
        # otherwise return an instance of Tokens.Float
        return Tokens.Integer(number) if not isFloat else Tokens.Float(number)

    def move(self) -> None:
        """
        Move the position pointer one step forward in the text and update the value of 'char' accordingly.
        Parameters:
            None
        Returns:
            None
        """
        self.position += 1
        if self.position < len(self.text):
            self.char = self.text[self.position]
