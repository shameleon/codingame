import sys


class RPN_Calculator:
    def __init__(self):
        self.stack = []
        self.ops = {
            'ADD': self.add,
            'SUB': self.substract,
            'MUL': self.multiply,
            'DIV': self.divide,
            'MOD': self.modulo,
            'POP': self.pop_nb,
            'DUP': self.dup_nb,
            'SWP': self.swap_stack,
            'ROT': self.rot_stack,
            'OVR': self.over_stack,
            'POS': self.pos_top_stack,
            'NOT': self.not_top_stack,
            'OUT': self.out_to_stdout
        }
        self.defs = {}

    def implement_instruction(self, token:str) -> None:
        print('s-----<', token, file=sys.stderr, flush=True)
        if token.lstrip('-').isdigit():
            self.stack.append(int(token))
        elif token in self.ops.keys():
            self.ops[token]()
        elif token in self.defs.keys():
            self.implement_def(token)
        else:
            return None
        print('       ', self.stack, file=sys.stderr, flush=True)
        return None
    
    def implement_def(self, def_name: str):
        tokens = self.defs[def_name].copy()
        i = 0
        while len(tokens) > 0:
            token = tokens.pop(0)
            self.implement_instruction(token)

    def rpn_operation(func):
        def wrapper(self):
            a = self.pop_nb()
            b = self.pop_nb()
            if a is not None and b is not None:
                self.push_nb(func(self, a, b))
        return wrapper

    @rpn_operation
    def add(self, a, b):
        return b + a

    @rpn_operation
    def substract(self, a, b):
        return b - a

    @rpn_operation
    def multiply(self, a, b):
        return b - a

    @rpn_operation
    def divide(self, a, b):
        if a != 0:
            return b // a
        else:
            raise ZeroDivisionError("Division by zero is undefined.")

    @rpn_operation
    def modulo(self, a, b):
        if a != 0:
            return b % a
        else:
            raise ZeroDivisionError("Modulo by zero is undefined.")

    def swap_stack(self):
        nb = self.pop_nb()
        pos = len(self.stack)
        self.stack.insert(pos - 1, nb)

    def pop_nb(self):
        return self.stack.pop() if self.stack else None
    
    def dup_nb(self):
        if not self.stack:
            return None
        a = int(self.stack[-1])
        if a != None:
            self.push_nb(a)
    
    def rot_stack(self):
        if not self.stack:
            return None
        nb = self.stack.pop(-3)
        self.stack.append(nb)

    def over_stack(self):
        if not self.stack:
            return None
        self.swap_stack()
        self.dup_nb()
        a = self.pop_nb()
        self.swap_stack()
        if a != None:
            self.push_nb(a)

    def pos_top_stack(self):
        if not self.stack:
            return None
        a = self.pop_nb()
        if a != None:
            self.push_nb([0, 1][a >= 0])
    
    def not_top_stack(self):
        if not self.stack:
            return None
        a = self.pop_nb()
        if a != None:
            self.push_nb([0, 1][a == 0])

    def push_nb(self, nb: int):
        self.stack.append(nb)

    def out_to_stdout(self):
        if not self.stack:
            return None
        res = self.stack.pop()
        print(res)

class ObsoleteProgrammer:
    def __init__(self):
        self.rpn = RPN_Calculator()
        self.def_buffer = []
        self.is_in_def = False

    def update_with_input(self, instructions: str):
        instructions = instructions.split()
        while len(instructions):
            token = instructions.pop(0)
            if token == 'DEF':
                self.is_in_def = True
            elif token == 'END':
                self.buffer_to_definition()
                self.is_in_def = False
            else :
                if self.is_in_def:
                    self.def_buffer.append(token)
                    print("b <----", self.def_buffer, file=sys.stderr, flush=True)
                else:
                    self.rpn.implement_instruction(token)

    def buffer_to_definition(self):
        def_name = self.def_buffer.pop(0)
        tmp = []
        while len(self.def_buffer):
            tmp.append(self.def_buffer.pop(0))
        self.rpn.defs[def_name] = list(tmp)
        print('def', def_name, self.rpn.defs[def_name], file=sys.stderr, flush=True)
        print("b <----", self.def_buffer, file=sys.stderr, flush=True)


def main():
    input_lines = [ '9 1 2 3 4 SWP',
                    'ROT DEF ZPR ADD SUB ROT MUL ADD',
                    'OUT END OUT 5 3 ZPR',
                    '2 MOD OUT']
    obsolete = ObsoleteProgrammer()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())

