class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def factor(self):
        if self.current_token.type in ["INTEGER", "FLOAT"]:
            return self.current_token
        elif self.current_token.value == "(":
            self.move()
            expression = self.expression()
            return expression

    def term(self):
        left_node = self.factor()
        self.move()
        while self.current_token.value == "*" or self.current_token.value == "/":
            operation = self.current_token
            self.move()
            right_node = self.factor()
            self.move()
            left_node = [left_node, operation, right_node]

        return left_node

    def expression(self):
        left_node = self.term()
        while self.current_token.value == "+" or self.current_token.value == "-":
            operation = self.current_token
            self.move()
            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def parser(self):
        return self.expression()

    def move(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
