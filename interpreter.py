from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from exprLexer import exprLexer
from exprParser import exprParser
from EvalVisitor import EvalVisitor


class SimpleErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Chyba syntaxe na pozici {line}:{column} - {msg}")


visitor = EvalVisitor()
error_listener = SimpleErrorListener()

print("Začni zadávat výrazy:")
while True:
    try:
        line = input('>> ')
        if not line.strip():
            continue

        line = line.replace("$", "\n")  # For my simulation of newlines in the console
        input_stream = InputStream(line + '\n')

        # Lexer
        lexer = exprLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        # Parser
        tokens = CommonTokenStream(lexer)
        parser = exprParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Parsování a vyhodnocení
        tree = parser.stat()
        result = visitor.visit(tree)

        if result is not None:
            print(result)

    except KeyboardInterrupt or EOFError:
        print("\nEnd!")
        break
    except Exception as e:
        print(f"Error: {str(e)}")


