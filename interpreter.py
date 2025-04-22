from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from exprLexer import exprLexer
from exprParser import exprParser
from EvalVisitor import EvalVisitor
from stack_interpreter import StackInterpreter
import sys
import os


class SimpleErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Chyba syntaxe na pozici {line}:{column} - {msg}")


def compare_files(generated_file, expected_file):
    try:
        with open(generated_file, 'r') as f1, open(expected_file, 'r') as f2:
            generated_lines = [line.strip() for line in f1 if line.strip()]
            expected_lines = [line.strip() for line in f2 if line.strip()]

            if len(generated_lines) != len(expected_lines):
                print(
                    f"Chyba: Počet instrukcí se neshoduje. Očekáváno: {len(expected_lines)}, Vygenerováno: {len(generated_lines)}")
                return False

            for i, (gen_line, exp_line) in enumerate(zip(generated_lines, expected_lines)):
                if gen_line != exp_line:
                    print(f"Chyba na řádku {i + 1}:")
                    print(f"  Očekáváno: {exp_line}")
                    print(f"  Generováno: {gen_line}")
                    return False

            return True
    except FileNotFoundError as e:
        print(f"Chyba při porovnávání souborů: {str(e)}")
        return False


def main():
    input_file = "input.txt"
    output_stack_file = "output.txt"
    expected_output_file = "expected_output.txt"

    try:
        print(f"Načítám zdrojový kód ze souboru {input_file}...")
        with open(input_file, 'r') as f:
            input_code = f.read()
        print(f"Načten soubor o velikosti {len(input_code)} znaků.")

        print("Vytvářím lexikální analyzer...")
        input_stream = InputStream(input_code)
        lexer = exprLexer(input_stream)
        error_listener = SimpleErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        print("Tokenizuji vstupní program...")
        tokens = CommonTokenStream(lexer)
        print("Vytvářím parser...")
        parser = exprParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        print("Parsování vstupního programu...")
        tree = parser.prog()
        print("Parsování dokončeno, začínám typovou kontrolu...")

        visitor = EvalVisitor()
        result = visitor.visit(tree)
        print("Typová kontrola proběhla úspěšně.")

        print("Generuji kód...")
        visitor.set_code_generation(True, output_stack_file)
        visitor.visit(tree)
        generated_code = visitor.get_code()
        visitor.save_code_to_file()

        print(f"Vygenerovaný kód byl uložen do souboru {output_stack_file}")
        print(f"Vygenerováno {len(generated_code)} instrukcí.")
        print("Vygenerované instrukce:")
        for instruction in generated_code:
            print(f"  {instruction}")

        if os.path.exists(expected_output_file):
            print(f"Porovnávám vygenerovaný kód s očekávaným výstupem ({expected_output_file})...")
            if compare_files(output_stack_file, expected_output_file):
                print("Test úspěšný! Vygenerovaný kód odpovídá očekávanému výstupu.")
            else:
                print("Test selhal! Vygenerovaný kód se neshoduje s očekávaným výstupem.")

        print("\nSpouštím generovaný kód:")
        interpreter = StackInterpreter()
        interpreter.load_program(output_stack_file)
        interpreter.execute()

    except Exception as e:
        print(f"Chyba: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
