import sys
import math

""" 50% success - 5 tests 5 validators out of 10 """


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
        self.is_in_cond_statement = False
        self.if_else_buffer = []


    def implement_instruction(self, token:str) -> None:
        if self.check_if_is_condition(token):
            return None
        print('s-----<', token, file=sys.stderr, flush=True)
        if token.lstrip('-').isdigit():
            self.stack.append(int(token))
        elif token in self.ops.keys():
            self.ops[token]()
        elif token in self.defs.keys():
            self.implement_def(token)
        elif token == 'IF':
            self.is_in_cond_statement = True
            self.if_else_buffer.append(token)
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

    def check_if_is_condition(self, token):
        if not self.is_in_cond_statement:
            return False
        self.if_else_buffer.append(token)
        if token == 'FI':
            self.is_in_cond_statement = False
            self.parse_condition(self.pop_nb())
        return True
    
    def parse_condition(self, cond_true: bool):
        before_else = True
        tmp = []
        while len(self.if_else_buffer):
            instr = self.if_else_buffer.pop(0)
            if instr == 'ELSE':
                before_else = False
            if instr not in ['IF', 'ELSE', 'FI']:
                if cond_true and before_else:
                    tmp.append(instr)
                elif not cond_true and not before_else:
                    tmp.append(instr)
        print('tmp---<', tmp, file=sys.stderr, flush=True)
 
    def add(self, a, b):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b + a)

    def substract(self, a, b):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b - a)

    def multiply(self, a, b):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b - a)

    def divide(self, a, b):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                if a != 0:
                    self.stack.append(b // a)

    def modulo(self, a, b):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                if a != 0:
                    self.stack.append(b % a)

    def swap_stack(self):
        nb = self.pop_nb()
        pos = len(self.stack)
        self.stack.insert(pos - 1, str(nb))

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

    def pop_nb(self):
        if not self.stack:
            return None
        nb = self.stack.pop()
        if nb.isdigit() or nb.lstrip('-').isdigit():
            return int(nb)
        return None

    def push_nb(self, nb: int):
        self.stack.append(str(nb))

    def out_to_stdout(self):
        if not self.stack:
            return None
        res = self.stack.pop()
        print(res)

def main():
    n = int(input())
    rpn = ObsoleteProgrammer()
    for i in range(n):
        instructions = input()
        print("######@", instructions, file=sys.stderr, flush=True)
        rpn.update_with_input(instructions)


if __name__ == '__main__':
    main()