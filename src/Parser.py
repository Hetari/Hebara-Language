import src.Tokens as Tokens


class Parser:
    def __init__(self, tokens: list[Tokens.Tokens]):
        """
        Initialize the class with the given list of tokens.

        Parameters:
            tokens (list): A list of tokens to be used by the class.

        Returns:
            None
        """
        self.tokens: list[Tokens.Tokens] = tokens
        self.position: int = 0
        self.current_token: Tokens.Tokens = self.tokens[self.position]

    def factor(self):
        """
        Determines the factor of the current token.

        Returns:
            Union[int, float, Expression]: The factor of the current token.
        """
        if self.current_token.type in ["INTEGER", "FLOAT"]:
            # That is the factor so return it
            return self.current_token

        elif self.current_token.value == "(":
            self.move()
            expression = self.expression()
            return expression

    def term(self) -> list[Tokens.Tokens]:
        """
        Evaluate a term expression.

        Returns:
            The evaluated result of the term expression.
        """
        # Get the left node of the term
        left_node = self.factor()

        # Move to the next token
        self.move()

        # Loop until there are no more multiplication or division operations
        while self.current_token.value in ["*", "/"]:
            # Get the operation token
            operation = self.current_token

            # Move to the next token
            self.move()

            # Get the right node of the term expression
            right_node = self.factor()

            # Move to the next token
            self.move()

            # Update the left node to include the current operation and right node
            left_node = [left_node, operation, right_node]

        # Return the evaluated result of the term expression
        return left_node

    def expression(self) -> list[Tokens.Tokens]:
        """
        Parses and evaluates an expression.

        Returns:
            The evaluated expression.
        """
        left_node = self.term()

        # Iterate while there are still addition or subtraction operators
        while self.current_token.value in ["+", "-"]:
            operation = self.current_token
            self.move()
            right_node = self.term()

            # Build a binary tree of the expression
            left_node = [left_node, operation, right_node]

        return left_node

    def parser(self):
        return self.expression()

    def move(self) -> None:
        """
        Move the position pointer one step forward in the tokens and update the value of 'current_token' accordingly.
        Parameters:
            None
        Returns:
            None
        """
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
