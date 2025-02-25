import re


def tokenize(expr: str) -> list:
    token_pattern = r"\d+|[+\-*/()]"
    return re.findall(token_pattern, expr)

def apply_oper(num: int, num2: int, op: str) -> int:
    if op == "+":
        return num + num2
    elif op == "-":
        return num - num2
    elif op == "*":
        return num * num2
    elif op == "/":
        if num2 == 0:
            raise ValueError(f"Chyba: výraz {num} {op} {num2} nemůže obsahovat 0 při dělení.")
        return num // num2
    else:
        raise ValueError(f"Neplatná operace: {op}.")

def find_matching_parenthesis(tokens: list, start_idx: int) -> int:
    depth = 1
    j = start_idx + 1

    while j < len(tokens) and depth > 0:
        if tokens[j] == "(":
            depth += 1
        elif tokens[j] == ")":
            depth -= 1
        j += 1

    if depth != 0:
        raise ValueError("Chyba: Špatně uzavřené závorky.")

    return j

def validate_tokens(tokens: list) -> None:
    if not tokens:
        return

    depth = 0
    for token in tokens:
        if token == "(":
            depth += 1
        elif token == ")":
            depth -= 1
            if depth < 0:
                raise ValueError("Chyba: Neplatné umístění uzavírací závorky.")

    if depth != 0:
        raise ValueError("Chyba: Špatně uzavřené závorky.")

def process_number(token: str) -> int:
    try:
        return int(token)
    except ValueError:
        raise ValueError(f"Chyba: {token} není číslo.")

def evaluate_parenthesis(tokens: list, i: int) -> (int, int):
    j = find_matching_parenthesis(tokens, i)
    subexpr_result = evaluate_expression(tokens[i + 1:j - 1])
    return subexpr_result, j

def handle_next_token_in_term(tokens: list, i: int, result: int, op: str) -> (int, str, int):
    token = tokens[i]

    if token == "(":
        subexpr_result, new_i = evaluate_parenthesis(tokens, i)

        if result is None:
            result = subexpr_result
        elif op in ["*", "/"]:
            result = apply_oper(result, subexpr_result, op)
            op = None
        else:
            return result, op, i

        i = new_i
    elif token in ["*", "/"]:
        op = token
        i += 1
    elif token in ["+", "-"]:
        if result is None:
            raise ValueError("Chyba: vícero znamének za sebou.")
        else:
            return result, op, i
    elif token != ")":
        num = process_number(token)

        if result is None:
            result = num
        elif op is not None:
            if op in ["*", "/"]:
                result = apply_oper(result, num, op)
                op = None
            else:
                return result, op, i
        else:
            raise ValueError("Chyba: Chybí operátor mezi čísly.")
        i += 1
    else:
        return result, op, i

    return result, op, i

def evaluate_term(tokens: list) -> (int, int):
    if not tokens:
        return None, 0

    result = None
    op = None
    i = 0

    while i < len(tokens):
        new_result, new_op, new_i = handle_next_token_in_term(tokens, i, result, op)

        if new_i == i:
            return result, i

        result = new_result
        op = new_op
        i = new_i

    return result, i

def handle_next_token_in_expression(tokens: list, i: int, result: int, op: str) -> (int, str, int):
    term_result, term_end = evaluate_term(tokens[i:])

    if term_end > 0:
        new_i = i + term_end
    else:
        new_i = len(tokens)

    if result is None:
        result = term_result
    elif op is not None:
        result = apply_oper(result, term_result, op)
        op = None

    if new_i < len(tokens):
        token = tokens[new_i]
        if token in ["+", "-"]:
            op = token
            new_i += 1
        elif token == ")":
            return result, op, new_i
        else:
            raise ValueError(f"Chyba: Chybí znaménko.")

    return result, op, new_i

def evaluate_expression(tokens: list) -> (int | None):
    if not tokens:
        return None

    validate_tokens(tokens)

    result = None
    op = None
    i = 0

    while i < len(tokens):
        result, op, i = handle_next_token_in_expression(tokens, i, result, op)

    if op is not None:
        raise ValueError("Chyba: Výraz končí operátorem.")

    return result

def process_text(text: str) -> None:
    tokens = tokenize(text)

    try:
        result = evaluate_expression(tokens)
        print(result)
    except ValueError as e:
        print(str(e))

def process_lines(lines_count: int) -> None:
    for i in range(lines_count):
        process_text(input())


def main() -> None:
    try:
        lines_count = int(input())
    except ValueError:
        print("Neplatný počet řádků.")
        return

    process_lines(lines_count)


if __name__ == "__main__":
    main()
