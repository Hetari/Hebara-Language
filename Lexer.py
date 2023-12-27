from Tokens import Boolean, Float, Integer, Operations, String


class Lexer:
    digits = "0123456789"
    operations = "+-/*()"
    ignore = ["#", "//", " "]

    #set a constructor
    def __init__(self, text):
        self.text = text
        #test = > user input
        self.pos = 0
        self.tokens = []
        #tokens = > terminal = > keywords
        self.char = self.text[self.pos]
        #once token is knows it will be added to tokens list
        self.token = None

    def tokenize(self):
        while self.pos < len(self.text):
                            #here cause didgits is static = > is accessed by class Lexer
            if self.char in Lexer.digits:
                # I did not understand it bro. extract_number ?? 
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                #check if input(char) is included in Operations
                self.token = Operations(self.char)
                self.move() # move to where ?? it does move to the next character using the position

            elif self.char in Lexer.ignore:
                self.move()
                continue

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.pos < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)

    def move(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.char = self.text[self.pos]
