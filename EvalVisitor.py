from antlr4 import *

if "." in __name__:
    from .exprParser import exprParser
    from .exprVisitor import exprVisitor
else:
    from exprParser import exprParser
    from exprVisitor import exprVisitor


class EvalVisitor(exprVisitor):
    def __init__(self):
        self.memory = {}
        self.types = {"int", "float", "string", "bool"}
        self.current_scope = {}
        self.scopes = [self.current_scope]
        self.output_file = None
        self.label_counter = 0
        self.code = []
        self.generate_code = False
        self._just_declared = set()

    def set_code_generation(self, generate, output_file=None):
        self.generate_code = generate
        self.output_file = output_file

        if generate:
            self.current_scope = {}
            self.scopes = [self.current_scope]
            self.memory = {}
            self.code = []
            self.label_counter = 0

    def get_code(self):
        return self.code

    def save_code_to_file(self):
        """Uloží vygenerovaný kód do souboru"""
        if self.output_file and self.code:
            with open(self.output_file, 'w') as f:
                for instruction in self.code:
                    f.write(instruction + '\n')
            return True
        return False

    def generate_new_label(self):
        """Generuje nové unikátní číslo pro návěští"""
        self.label_counter += 1
        return self.label_counter - 1

    def type_to_code(self, type_str):
        """Převádí typ na kód pro instrukce"""
        if type_str == "int":
            return "I"
        elif type_str == "float":
            return "F"
        elif type_str == "bool":
            return "B"
        elif type_str == "string":
            return "S"
        else:
            raise Exception(f"Neznámý typ '{type_str}'")

    def default_value_for_type(self, var_type: str):
        if var_type == "int":
            return 0
        elif var_type == "float":
            return 0.0
        elif var_type == "bool":
            return "false"
        elif var_type == "string":
            return '""'
        elif var_type == "file":
            return "./"
        else:
            raise Exception(f"Unknown type '{var_type}'")

    def check_type(self, expected_type: str, actual_value, context_info=""):
        actual_type = self.type_of_value(actual_value)
        if expected_type == "file" and actual_type == "string":
            return

        if expected_type != actual_type:
            raise Exception(
                f"Type mismatch{f' in {context_info}' if context_info else ''}: expected {expected_type}, got {actual_type}")

    def type_of_value(self, value):
        if isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            return "string"
        else:
            raise Exception(f"Unsupported value type: {type(value)}")

    def visitProg(self, ctx: exprParser.ProgContext):
        results = []
        for stat in ctx.stat():
            result = self.visit(stat)
            if result is not None:
                results.append(result)
        return results

    def visitDeclar(self, ctx):
        decl_ctx = ctx.decl()

        if hasattr(decl_ctx, 'vartype') and callable(getattr(decl_ctx, 'vartype')):
            var_type_ctx = decl_ctx.vartype()
            declared_type = var_type_ctx.getText().lower()

            var_type = None
            if declared_type == "int":
                var_type = "int"
            elif declared_type == "float":
                var_type = "float"
            elif declared_type == "string":
                var_type = "string"
            elif declared_type == "bool":
                var_type = "bool"
            else:
                raise Exception(f"Neznámý typ: {declared_type}")

            if hasattr(decl_ctx, 'ID') and callable(getattr(decl_ctx, 'ID')):
                id_token = decl_ctx.ID()

                if hasattr(id_token, '__iter__') and not isinstance(id_token, str):
                    for id_node in id_token:
                        variable_id = id_node.getText()

                        if variable_id in self.current_scope and not self.generate_code:
                            raise Exception(f"Proměnná {variable_id} již byla deklarována")

                        self.current_scope[variable_id] = var_type
                        self._just_declared.add(variable_id)

                        if self.generate_code:
                            default_value = self.default_value_for_type(var_type)
                            type_code = self.type_to_code(var_type)
                            self.code.append(f"push {type_code} {default_value}")
                            self.code.append(f"save {variable_id}")
                else:
                    variable_id = id_token.getText()

                    if variable_id in self.current_scope and not self.generate_code:
                        raise Exception(f"Proměnná {variable_id} již byla deklarována")

                    self.current_scope[variable_id] = var_type
                    self._just_declared.add(variable_id)

                    if self.generate_code:
                        default_value = self.default_value_for_type(var_type)
                        type_code = self.type_to_code(var_type)
                        self.code.append(f"push {type_code} {default_value}")
                        self.code.append(f"save {variable_id}")

        return None

    def visitAssign(self, ctx):
        variable_id = ctx.ID().getText()
        expression = ctx.expr()

        var_type = self.check_variable_type(variable_id)
        expr_result = self.visit(expression)
        expr_type = self.type_of_value(expr_result)

        if var_type == "int" and expr_type == "float":
            raise Exception(f"Nelze přiřadit float do int")

        if self.generate_code:
            if var_type == "float" and expr_type == "int":
                self.code.append("itof")
                self.code.append(f"save {variable_id}")
            else:
                self.code.append(f"save {variable_id}")

            self.code.append(f"load {variable_id}")
            self.code.append("pop")

        return None

    def visitPrintvar(self, ctx: exprParser.PrintvarContext):
        value = self.visit(ctx.expr())

        if self.generate_code:
            self.code.append("print 1")

        return value

    def visitBool(self, ctx):
        value = ctx.BOOL().getText().lower()

        if self.generate_code:
            self.code.append(f"push B {value}")

        if value == "true":
            return True
        else:
            return False

    def visitString(self, ctx: exprParser.StringContext):
        string_val = ctx.STRING().getText()
        value = string_val[1:-1]

        if self.generate_code:
            self.code.append(f"push S {string_val}")

        return value

    def visitVar(self, ctx):
        var_name = ctx.ID().getText()

        found = False
        var_type = None

        if var_name in self.current_scope:
            found = True
            var_type = self.current_scope[var_name]
        else:
            for scope in self.scopes:
                if var_name in scope:
                    found = True
                    var_type = scope[var_name]
                    break

        if not found:
            raise Exception(f"Variable '{var_name}' used before declaration.")

        if self.generate_code:
            self.code.append(f"load {var_name}")

        if var_type == "int":
            return 0
        elif var_type == "float":
            return 0.0
        elif var_type == "string":
            return ""
        elif var_type == "bool":
            return False
        else:
            return None

    def visitInt(self, ctx: exprParser.IntContext):
        value = int(ctx.INT().getText())

        if self.generate_code:
            self.code.append(f"push I {value}")

        return value

    def visitFloat(self, ctx: exprParser.FloatContext):
        value = float(ctx.FLOAT().getText())

        if self.generate_code:
            self.code.append(f"push F {value}")

        return value

    def visitFile(self, ctx: exprParser.FileContext):
        return str(ctx.FILE().getText())[1:-1]

    def visitParantheses(self, ctx: exprParser.ParanthesesContext):
        return self.visit(ctx.expr())

    def visitLogicnot(self, ctx: exprParser.LogicnotContext):
        value = self.visit(ctx.expr())
        self.check_type("bool", value, "logical NOT")

        if self.generate_code:
            self.code.append("not")

        return not value

    def visitAddsub(self, ctx: exprParser.AddsubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Operator '{op}' used with non-numeric value: {val}")

        type_code = "I" if isinstance(left, int) and isinstance(right, int) else "F"

        if isinstance(left, int) and isinstance(right, float) and self.generate_code:
            self.code.append("save __temp__")
            self.code.append(f"push I {left}")
            self.code.append("itof")
            self.code.append("load __temp__")

        if isinstance(left, float) and isinstance(right, int) and self.generate_code:
            self.code.append("itof")

        if self.generate_code:
            if op == "+":
                self.code.append(f"add {type_code}")
            else:
                self.code.append(f"sub {type_code}")

        return left + right if op == "+" else left - right

    def visitStringconcat(self, ctx: exprParser.StringconcatContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if not isinstance(left, str) or not isinstance(right, str):
            raise Exception(f"String concatenation used with non-string values: {left}, {right}")

        if self.generate_code:
            self.code.append("concat")

        return left + right

    def visitAssignexpr(self, ctx):
        variable_id = ctx.ID().getText()
        variable_type = self.check_variable_type(variable_id)
        expr_value = self.visit(ctx.expr())

        if expr_value is None:
            return

        expr_type = self.type_of_value(expr_value)

        if expr_type == "int" and variable_type == "float":
            if self.generate_code:
                self.code.append("itof")
            expr_type = "float"

        if expr_type != variable_type:
            raise Exception(f"Chyba: Nelze přiřadit hodnotu typu {expr_type} do proměnné typu {variable_type}")

        if self.generate_code:
            self.code.append(f"save {variable_id}")

            self.code.append(f"load {variable_id}")

        return expr_value

    def visitUnaryminus(self, ctx: exprParser.UnaryminusContext):
        value = self.visit(ctx.expr())
        if not isinstance(value, (int, float)):
            raise Exception(f"Unary minus used on non-numeric value: {value}")

        if self.generate_code:
            type_code = "I" if isinstance(value, int) else "F"
            self.code.append(f"uminus {type_code}")

        return -value

    def visitMuldiv(self, ctx: exprParser.MuldivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Operator '{op}' used with non-numeric value: {val}")

        if op == "%" and (isinstance(left, float) or isinstance(right, float)):
            raise Exception("Modulo operation not supported for float values")

        type_code = "I" if isinstance(left, int) and isinstance(right, int) else "F"

        if isinstance(left, int) and isinstance(right, float) and self.generate_code:
            self.code.append("save __temp__")
            self.code.append(f"push I {left}")
            self.code.append("itof")
            self.code.append("load __temp__")

        if isinstance(left, float) and isinstance(right, int) and self.generate_code:
            self.code.append("itof")

        if self.generate_code:
            if op == "*":
                self.code.append(f"mul {type_code}")
            elif op == "/":
                self.code.append(f"div {type_code}")
            elif op == "%" and type_code == "I":
                self.code.append("mod")
            elif op == "%" and type_code == "F":
                raise Exception("Modulo operation not supported for float values")

        if op == "*":
            return left * right
        elif op == "/":
            return left / right
        elif op == "%":
            return left % right

    def visitLogicor(self, ctx: exprParser.LogicorContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        for val in (left, right):
            self.check_type("bool", val, "logical OR")

        if self.generate_code:
            self.code.append("or")

        return left or right

    def visitLogicand(self, ctx: exprParser.LogicandContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        for val in (left, right):
            self.check_type("bool", val, "logical AND")

        if self.generate_code:
            self.code.append("and")

        return left and right

    def visitCompare(self, ctx: exprParser.CompareContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Comparison '{op}' used with non-numeric value: {val}")

        type_code = "I" if isinstance(left, int) and isinstance(right, int) else "F"

        if self.generate_code and isinstance(left, int) and isinstance(right, float):
            push_left_index = None
            push_right_index = None

            for i in range(len(self.code) - 1, -1, -1):
                if "push" in self.code[i]:
                    if push_right_index is None:
                        push_right_index = i
                    else:
                        push_left_index = i
                        break

            if push_left_index is not None and push_right_index is not None:
                self.code.insert(push_left_index + 1, "itof")

                push_right = self.code.pop(push_right_index + 1)
                self.code.append(push_right)

        if self.generate_code:
            if op == "<":
                self.code.append(f"lt {type_code}")
            elif op == ">":
                self.code.append(f"gt {type_code}")

        if op == "<":
            return left < right
        elif op == ">":
            return left > right

    def visitIsequal(self, ctx: exprParser.IsequalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if isinstance(left, int) and isinstance(right, int):
            type_code = "I"
        elif isinstance(left, float) or isinstance(right, float):
            type_code = "F"

            if isinstance(left, int) and self.generate_code:
                self.code.append("itof")
            elif isinstance(right, int) and self.generate_code:
                self.code.append("itof")
        elif isinstance(left, str) and isinstance(right, str):
            type_code = "S"
        else:
            raise Exception(f"Equality operator '{op}' used with incompatible types: {type(left)} and {type(right)}")

        if self.generate_code:
            self.code.append(f"eq {type_code}")
            if op == "!=":
                self.code.append("not")

        if op == "==":
            return left == right
        elif op == "!=":
            return left != right

    def visitIfstatement(self, ctx):
        else_label = self.generate_new_label()
        end_label = self.generate_new_label()

        condition = self.visit(ctx.expr())
        self.check_type("bool", condition, "if condition")

        if self.generate_code:
            self.code.append(f"fjmp {else_label}")

        if condition or self.generate_code:
            then_start_idx = 4

            if ctx.getChild(then_start_idx).getText() == '{':
                new_scope = {}
                self.scopes.append(new_scope)
                self.current_scope = new_scope

                then_start = then_start_idx + 1
                then_end = then_start
                while then_end < ctx.getChildCount() and ctx.getChild(then_end).getText() != '}':
                    then_end += 1

                for i in range(then_start, then_end):
                    self.visit(ctx.getChild(i))

                self.scopes.pop()
                self.current_scope = self.scopes[-1]
            else:

                self.visit(ctx.getChild(then_start_idx))

            if self.generate_code:
                self.code.append(f"jmp {end_label}")
                self.code.append(f"label {else_label}")

        has_else = False
        for i in range(ctx.getChildCount()):
            if ctx.getChild(i).getText() == 'else':
                has_else = True
                if not condition or self.generate_code:

                    new_scope = {}
                    self.scopes.append(new_scope)
                    self.current_scope = new_scope

                    else_idx = i + 1

                    if else_idx < ctx.getChildCount() and ctx.getChild(else_idx).getText() == '{':
                        else_start = else_idx + 1
                        else_end = else_start
                        while else_end < ctx.getChildCount() and ctx.getChild(else_end).getText() != '}':
                            else_end += 1

                        for j in range(else_start, else_end):
                            self.visit(ctx.getChild(j))
                    else:

                        self.visit(ctx.getChild(else_idx))

                    self.scopes.pop()
                    self.current_scope = self.scopes[-1]
                break

        if self.generate_code:
            self.code.append(f"label {end_label}")

        return None

    def visitMultistatement(self, ctx):
        new_scope = {}
        self.scopes.append(new_scope)
        self.current_scope = new_scope

        results = []
        for stat in ctx.stat():
            result = self.visit(stat)
            if result is not None:
                results.append(result)

        self.scopes.pop()
        self.current_scope = self.scopes[-1]

        return results

    def visitWhile(self, ctx: exprParser.WhileContext):
        start_label = self.generate_new_label()
        end_label = self.generate_new_label()

        if self.generate_code:
            self.code.append(f"label {start_label}")

        condition = self.visit(ctx.expr())
        self.check_type("bool", condition, "while condition")

        if self.generate_code:
            self.code.append(f"fjmp {end_label}")

        results = []
        if condition or self.generate_code:
            new_scope = {}
            self.scopes.append(new_scope)
            self.current_scope = new_scope

            block_results = []
            for stat in ctx.stat():
                result = self.visit(stat)
                if result is not None:
                    block_results.append(result)

            results.append(block_results)

            self.scopes.pop()
            self.current_scope = self.scopes[-1]

            if self.generate_code:
                self.code.append(f"jmp {start_label}")
                self.code.append(f"label {end_label}")
                return results

        return results

    def visitRead(self, ctx):
        id_tokens = ctx.ID()

        if isinstance(id_tokens, list):
            variable_ids = [token.getText() for token in id_tokens]
        else:
            variable_ids = [id_tokens.getText()]

        for variable_id in variable_ids:
            var_type = self.check_variable_type(variable_id)

            if self.generate_code:
                self.code.append(f"read {self.type_to_code(var_type)}")
                self.code.append(f"save {variable_id}")

        return None

    def visitWrite(self, ctx: exprParser.WriteContext):
        expr_count = len(ctx.expr())
        values = []

        for expr in ctx.expr():
            val = self.visit(expr)
            values.append(str(val))

        if self.generate_code:
            self.code.append(f"print {expr_count}")

        output = " ".join(values)
        return output


    def visitAssignMultiple(self, ctx):

        variable_ids = []
        if ctx.ID():
            variable_ids.append(ctx.ID().getText())
        if ctx.id_list():
            for id_node in ctx.id_list().ID():
                variable_ids.append(id_node.getText())

        expr_value = self.visit(ctx.expr())
        if expr_value is None:
            return None

        expr_type = self.type_of_value(expr_value)

        for variable_id in variable_ids:
            var_type = self.check_type(variable_id)
            if expr_type != var_type:
                if not (expr_type == "int" and var_type == "float"):
                    raise Exception(f"Nelze přiřadit hodnotu typu {expr_type} do proměnné typu {var_type}")

        if self.generate_code:

            last_var = variable_ids[-1]
            last_var_type = self.check_type(last_var)

            if expr_type == "int" and last_var_type == "float":
                self.code.append("itof")

            self.code.append(f"save {last_var}")

            for i in range(len(variable_ids) - 2, -1, -1):
                var_id = variable_ids[i]
                var_type = self.check_type(var_id)

                prev_var = variable_ids[i + 1]
                self.code.append(f"load {prev_var}")

                if expr_type == "int" and var_type == "float":
                    self.code.append("itof")

                self.code.append(f"save {var_id}")

            self.code.append(f"load {variable_ids[0]}")
            self.code.append("pop")

        return expr_value

    def check_variable_type(self, variable_id, actual_value=None):
        if variable_id not in self.current_scope:
            for scope in self.scopes:
                if variable_id in scope:
                    return scope[variable_id]
            raise Exception(f"Proměnná {variable_id} nebyla deklarována")

        variable_type = self.current_scope[variable_id]

        if actual_value is not None:
            value_type = self.type_of_value(actual_value)
            if variable_type != value_type and not (variable_type == "float" and value_type == "int"):
                raise Exception(
                    f"Typová neshoda: {variable_id} je typu {variable_type}, ale přiřazovaná hodnota je typu {value_type}")

        return variable_type

    def visitFilewrite(self, ctx: exprParser.FilewriteContext):
        var_name = ctx.ID().getText()
        var_type = self.types[var_name]

        if var_name not in self.memory:
            raise Exception(f"Variable '{var_name}' not declared before write.")

        if var_type != "file":
            raise Exception(f"Unsupported type '{var_type}' in write")

        expr_written = []
        for expr in ctx.expr():
            value = self.visit(expr)
            expr_type = self.type_of_value(value)

            if expr_type not in ["int", "float", "string"]:
                raise Exception(f"Unsupported type '{expr_type}' in write")
            expr_written.append(value)

        return expr_written