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
        self.types = {}
        self.current_scope = {}
        self.scopes = [self.current_scope]

    def default_value_for_type(self, var_type: str):
        if var_type == "int":
            return 0
        elif var_type == "float":
            return 0.0
        elif var_type == "bool":
            return False
        elif var_type == "string":
            return ""
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

    def visitDeclar(self, ctx: exprParser.DeclarContext):
        decl_ctx = ctx.decl()
        var_type = decl_ctx.vartype().getText()
        vars = decl_ctx.ID()

        for var in vars:
            if var.getText() in self.memory:
                raise Exception(f"Variable '{var.getText()}' is already declared")

        if decl_ctx.expr():
            value = self.visit(decl_ctx.expr())
            # exception that if we assign 5 it will be 5.0
            if var_type == "float" and isinstance(value, int) and not isinstance(value, bool):
                value = float(value)
            else:
                self.check_type(var_type, value, f"declaration of {vars[0].getText()}")
        else:
            value = self.default_value_for_type(var_type)

        for var in vars:
            var_name = var.getText()
            self.memory[var_name] = value
            self.types[var_name] = var_type

        if decl_ctx.expr():
            return f"{var_type} " + ', '.join([var.getText() for var in vars]) + f" = {value}"
        else:
            return f"{var_type} " + ', '.join([var.getText() for var in vars]) + f" (výchozí hodnota: {value})"

    def visitAssign(self, ctx: exprParser.AssignContext):
        var_name = ctx.ID().getText()

        if var_name not in self.memory:
            raise Exception(f"Assignment to undeclared variable '{var_name}'")

        value = self.visit(ctx.expr())
        expected_type = self.types[var_name]

        # exception that if we assign 5 it will be 5.0
        if expected_type == "float" and isinstance(value, int) and not isinstance(value, bool):
            value = float(value)
        else:
            self.check_type(expected_type, value, f"assignment to {var_name}")
        self.memory[var_name] = value
        return f"{var_name} = {value}"

    def visitPrintvar(self, ctx: exprParser.PrintvarContext):
        return self.visit(ctx.expr())

    def visitBool(self, ctx: exprParser.BoolContext):
        return ctx.BOOL().getText() == "true"

    def visitString(self, ctx: exprParser.StringContext):
        return ctx.STRING().getText()[1:-1]

    def visitVar(self, ctx: exprParser.VarContext):
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            raise Exception(f"Variable '{var_name}' used before declaration.")
        return self.memory[var_name]

    def visitInt(self, ctx: exprParser.IntContext):
        return int(ctx.INT().getText())

    def visitFloat(self, ctx: exprParser.FloatContext):
        return float(ctx.FLOAT().getText())

    def visitFile(self, ctx: exprParser.FileContext):
        return str(ctx.FILE().getText())[1:-1]

    def visitParantheses(self, ctx: exprParser.ParanthesesContext):
        return self.visit(ctx.expr())

    def visitLogicnot(self, ctx: exprParser.LogicnotContext):
        value = self.visit(ctx.expr())
        self.check_type("bool", value, "logical NOT")
        return not value

    def visitAddsub(self, ctx: exprParser.AddsubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Operator '{op}' used with non-numeric value: {val}")

        return left + right if op == "+" else left - right

    def visitStringconcat(self, ctx: exprParser.StringconcatContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if not isinstance(left, str) or not isinstance(right, str):
            raise Exception(f"String concatenation used with non-string values: {left}, {right}")
        return left + right

    def visitAssignexpr(self, ctx: exprParser.AssignexprContext):
        var_name = ctx.ID().getText()

        if var_name not in self.memory:
            raise Exception(f"Assignment to undeclared variable '{var_name}'")

        value = self.visit(ctx.expr())
        expected_type = self.types[var_name]
        self.check_type(expected_type, value, f"expression-assignment to {var_name}")
        self.memory[var_name] = value

        return value

    def visitUnaryminus(self, ctx: exprParser.UnaryminusContext):
        value = self.visit(ctx.expr())
        if not isinstance(value, (int, float)):
            raise Exception(f"Unary minus used on non-numeric value: {value}")
        return -value

    def visitMuldiv(self, ctx: exprParser.MuldivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Operator '{op}' used with non-numeric value: {val}")

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
        return left or right

    def visitLogicand(self, ctx: exprParser.LogicandContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        for val in (left, right):
            self.check_type("bool", val, "logical AND")
        return left and right

    def visitCompare(self, ctx: exprParser.CompareContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        for val in (left, right):
            if not isinstance(val, (int, float)):
                raise Exception(f"Comparison '{op}' used with non-numeric value: {val}")

        if op == "<":
            return left < right
        elif op == ">":
            return left > right

    def visitIsequal(self, ctx: exprParser.IsequalContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == "==":
            return left == right
        elif op == "!=":
            return left != right

    def visitIfstatement(self, ctx):
        condition = self.visit(ctx.expr())
        self.check_type("bool", condition, "if condition")

        def execute_block(start_index, end_marker='}'):
            new_scope = {}
            self.scopes.append(new_scope)
            self.current_scope = new_scope

            results = []
            i = start_index
            while i < ctx.getChildCount() and ctx.getChild(i).getText() != end_marker:
                result = self.visit(ctx.getChild(i))
                if result is not None:
                    results.append(result)
                i += 1

            self.scopes.pop()
            self.current_scope = self.scopes[-1]
            return results

        if condition:
            return execute_block(5)
        else:
            for i in range(ctx.getChildCount()):
                if ctx.getChild(i).getText() == 'else':
                    return execute_block(i + 2)

        return []

    def visitMultistatement(self, ctx: exprParser.MultistatementContext):
        new_scope = {}
        self.scopes.append(new_scope)
        self.current_scope = new_scope

        results = []
        for i in range(1, ctx.getChildCount() - 1):
            result = self.visit(ctx.getChild(i))
            if result is not None:
                results.append(result)

        self.scopes.pop()
        self.current_scope = self.scopes[-1]

        return results

    def visitWhile(self, ctx: exprParser.WhileContext):
        results = []

        while True:
            condition = self.visit(ctx.expr())
            self.check_type("bool", condition, "while condition")

            if not condition:
                break

            new_scope = {}
            self.scopes.append(new_scope)
            self.current_scope = new_scope

            block_results = []
            for i in range(5, ctx.getChildCount() - 1):
                if ctx.getChild(i).getText() != '}':
                    result = self.visit(ctx.getChild(i))
                    if result is not None:
                        block_results.append(result)

            results.append(block_results)

            self.scopes.pop()
            self.current_scope = self.scopes[-1]

        return results

    def visitRead(self, ctx: exprParser.ReadContext):
        var_names = [var.getText() for var in ctx.ID()]
        for var_name in var_names:
            if var_name not in self.memory:
                raise Exception(f"Variable '{var_name}' not declared before read.")
            expected_type = self.types[var_name]
            raw_input = input()

            try:
                if expected_type == "int":
                    value = int(raw_input)
                elif expected_type == "float":
                    value = float(raw_input)
                elif expected_type == "bool":
                    if raw_input.lower() in ["true", "false"]:
                        value = raw_input.lower() == "true"
                    else:
                        raise ValueError("Invalid boolean value")
                elif expected_type == "string":
                    value = raw_input
                else:
                    raise Exception(f"Unsupported type '{expected_type}' in read")
            except ValueError:
                raise Exception(
                    f"Input value '{raw_input}' for variable '{var_name}' is not of expected type '{expected_type}'")

            self.memory[var_name] = value

        return f"Read input for: {', '.join(var_names)}"

    def visitWrite(self, ctx: exprParser.WriteContext):
        values = []
        for expr in ctx.expr():
            val = self.visit(expr)
            values.append(str(val))
        output = " ".join(values)
        return output

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