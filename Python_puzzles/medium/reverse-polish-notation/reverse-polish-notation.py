import sys
import math

""" 100% success"""

class ReversePolishNotation:
    def __init__(self, instructions: list):
        self.instructions = instructions
        self.stack = []
        self.ops = {'ADD': self.add,
                    'MUL': self.multiply,
                    'SUB': self.substract,
                    'DIV': self.divide,
                    'MOD': self.modulo,
                    'POP': self.pop_nb,
                    'DUP': self.dup_nb,
                    'SWP': self.swap_stack,
                    'ROL': self.roll_stack
                   }
        self.read_instructions()

    def read_instructions(self) -> None:
        if not self.instructions:
            return None
        instruction = self.instructions.pop(0)
        print('ins=', instruction, file=sys.stderr, flush=True)
        if instruction.lstrip('-').isdigit():
            self.stack.append(instruction)
        elif instruction in self.ops.keys():
            self.ops[instruction]()
        print(self.stack, file=sys.stderr, flush=True)
        self.read_instructions()
        return None

    def pop_nb(self):
        if not self.stack:
            return None
        nb = self.stack.pop()
        if nb.isdigit() or nb.lstrip('-').isdigit():
            return int(nb)
        return None

    def dup_nb(self):
        if not self.stack:
            self.stack.append('ERROR')
            return None
        self.push_nb(self.stack[-1])

    def push_nb(self, nb: int):
        self.stack.append(str(nb))

    def add(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a and b:
            self.push_nb(a + b)
        else:
            self.stack.append('ERROR')

    def multiply(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a and b:
            self.push_nb(a * b)
        else:
            self.stack.append('ERROR')

    def substract(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a and b:
            self.push_nb(b - a)
        else:
            self.stack.append('ERROR')

    def divide(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a and b and b != 0:
            self.push_nb(b // a)
        else:
            self.stack.append('ERROR')

    def modulo(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a and b and b != 0:
            self.push_nb(b % a)
        else:
            self.stack.append('ERROR')

    def swap_stack(self):
        nb = self.pop_nb()
        pos = len(self.stack)
        self.stack.insert(pos - 1, str(nb))

    def roll_stack(self):
        nb = self.pop_nb()
        if nb:
            pos = len(self.stack) - nb
            if pos >= 0 and nb > 0:
                element = self.stack.pop(pos)
                self.stack.append(element)
            else:
                self.stack.append('ERROR')

    def __repr__(self):
        return f'{" ".join(self.stack)}'


def main():
    n = int(input())
    instructions = input().split()
    print(' '.join(instructions), file=sys.stderr, flush=True)
    rpn = ReversePolishNotation(instructions)
    print(rpn)


if __name__ == '__main__':
    main()