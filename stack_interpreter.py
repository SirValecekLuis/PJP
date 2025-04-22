class StackInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.labels = {}
        self.instruction_pointer = 0
        self.instructions = []

    def load_program(self, filename):
        """Načte program ze souboru a najde všechna návěští"""
        with open(filename, 'r') as f:
            self.instructions = [line.strip() for line in f if line.strip()]

        # Najít všechny návěští v programu
        for i, instruction in enumerate(self.instructions):
            parts = instruction.split()
            if parts[0] == "label":
                label_num = int(parts[1])
                self.labels[label_num] = i

    def execute(self):
        """Provede všechny instrukce programu"""
        self.instruction_pointer = 0
        while self.instruction_pointer < len(self.instructions):
            instruction = self.instructions[self.instruction_pointer]
            self.execute_instruction(instruction)
            self.instruction_pointer += 1

    def execute_instruction(self, instruction):
        """Provede jednu instrukci"""
        parts = instruction.split()
        cmd = parts[0]

        # Aritmetické operace
        if cmd == "add":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)

        elif cmd == "sub":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a - b)

        elif cmd == "mul":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a * b)

        elif cmd == "div":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a / b)

        elif cmd == "mod":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a % b)

        elif cmd == "uminus":
            type_code = parts[1]
            a = self.stack.pop()
            self.stack.append(-a)

        # String operace
        elif cmd == "concat":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a + b)

        # Logické operace
        elif cmd == "and":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a and b)

        elif cmd == "or":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a or b)

        # Porovnávací operace
        elif cmd == "gt":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a > b)

        elif cmd == "lt":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a < b)

        elif cmd == "eq":
            type_code = parts[1]
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append(a == b)

        elif cmd == "not":
            a = self.stack.pop()
            self.stack.append(not a)

        # Konverze typů
        elif cmd == "itof":
            a = self.stack.pop()
            self.stack.append(float(a))

        # Práce se zásobníkem
        elif cmd == "push":
            type_code = parts[1]
            value = ' '.join(parts[2:])

            if type_code == "I":
                self.stack.append(int(value))
            elif type_code == "F":
                self.stack.append(float(value))
            elif type_code == "B":
                self.stack.append(value.lower() == "true")
            elif type_code == "S":
                # Odstranit uvozovky, pokud existují
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                self.stack.append(value)

        elif cmd == "pop":
            self.stack.pop()

        # Práce s proměnnými
        elif cmd == "load":
            var_name = parts[1]
            if var_name in self.variables:
                self.stack.append(self.variables[var_name])
            else:
                raise Exception(f"Nedeklarovaná proměnná '{var_name}'")

        elif cmd == "save":
            var_name = parts[1]
            self.variables[var_name] = self.stack.pop()

        # Návěští a skoky
        elif cmd == "label":
            # Již zpracováno během načítání programu
            pass

        elif cmd == "jmp":
            label_num = int(parts[1])
            if label_num in self.labels:
                self.instruction_pointer = self.labels[label_num] - 1  # -1 protože po provedení se zvedne o 1
            else:
                raise Exception(f"Návěští {label_num} nenalezeno")

        elif cmd == "fjmp":
            label_num = int(parts[1])
            condition = self.stack.pop()
            if not condition:
                if label_num in self.labels:
                    self.instruction_pointer = self.labels[label_num] - 1
                else:
                    raise Exception(f"Návěští {label_num} nenalezeno")

        # I/O operace
        elif cmd == "print":
            n = int(parts[1])
            values = []
            for _ in range(n):
                values.insert(0, str(self.stack.pop()))
            print(' '.join(values))

        elif cmd == "read":
            type_code = parts[1]
            raw_input = input()

            try:
                if type_code == "I":
                    self.stack.append(int(raw_input))
                elif type_code == "F":
                    self.stack.append(float(raw_input))
                elif type_code == "B":
                    if raw_input.lower() in ["true", "false"]:
                        self.stack.append(raw_input.lower() == "true")
                    else:
                        raise ValueError("Neplatná boolean hodnota")
                elif type_code == "S":
                    self.stack.append(raw_input)
            except ValueError:
                raise Exception(f"Vstupní hodnota '{raw_input}' neodpovídá očekávanému typu '{type_code}'")

        else:
            raise Exception(f"Neznámá instrukce: {cmd}")
