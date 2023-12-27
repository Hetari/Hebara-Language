class Tokens:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Tokens):
    def __init__(self, value):
        super().__init__("INTEGER", value)


class String(Tokens):
    def __init__(self, value):
        super().__init__("STRING", value)


class Boolean(Tokens):
    def __init__(self, value):
        super().__init__("BOOLEAN", value)


class Float(Tokens):
    def __init__(self, value):
        super().__init__("FLOAT", value)


class Operations(Tokens):
    def __init__(self, value):
        super().__init__("OP", value)
