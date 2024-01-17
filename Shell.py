import Lexer
import Parser
import Interpreter
import os


# Main loop for the interpreter
while True:
    try:
        # Prompt the user for input
        text = input("Hebara >> ")
    except KeyboardInterrupt:
        # Handle keyboard interrupt
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("Good bye!")
        break
    else:
        # Tokenize the input text
        tokenizer = Lexer.Lexer(text)
        tokens = tokenizer.tokenize()

        # Parse the tokens into an abstract syntax tree
        parser = Parser.Parser(tokens)
        tree = parser.parser()

        # Interpret the abstract syntax tree
        interpreter = Interpreter.Interpreter(tree)
        res = interpreter.interpret()

        # Print the result
        print(res)
