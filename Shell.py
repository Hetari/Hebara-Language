import Lexer
import Parser
import Interpreter
import os

while True:
    try:
        text = input("Hebara >> ")
    except KeyboardInterrupt:
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("Good bey!")
        break
    else:
        tokenizer = Lexer.Lexer(text)
        tokens = tokenizer.tokenize()

        parser = Parser.Parser(tokens)
        tree = parser.parser()

        interpreter = Interpreter.Interpreter(tree)

        res = interpreter.interpret()
        print(res)
