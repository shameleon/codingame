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
        self.is_in_cond_statement = False
        self.if_else_buffer = []


    def implement_instruction(self, token:str) -> None:
        if self.check_if_is_condition(token):
            return None
        if token.lstrip('-').isdigit():
            print('push  >', token, file=sys.stderr, flush=True)
            self.stack.append(int(token))
        elif token in self.ops.keys():
            print('ops   >', token, file=sys.stderr, flush=True)
            self.ops[token]()
        elif token in self.defs.keys():
            print('def   >', token, file=sys.stderr, flush=True)
            self.implement_def(token)
        elif token == 'IF':
            self.is_in_cond_statement = True
            self.if_else_buffer.append(token)
        else:
            return None
        print('             ', self.stack, file=sys.stderr, flush=True)
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
            self.parse_condition(bool(self.pop_nb()))
        return True
    
    def parse_condition(self, cond_true: bool):
        before_else = True
        tmp = []
        while len(self.if_else_buffer):
            instr = self.if_else_buffer.pop(0)
            if instr == 'ELSE':
                before_else = False
            elif instr not in ['IF', 'ELSE', 'FI']:
                if cond_true and before_else:
                    tmp.append(instr)
                elif not cond_true and not before_else:
                    tmp.append(instr)
            elif instr == 'FI':
                while len(self.if_else_buffer) > 0:
                    self.is_in_cond_statement = False
                    self.implement_instruction(self.if_else_buffer.pop())
        print('if_else buffer = ', tmp, file=sys.stderr, flush=True)
            
    def add(self):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b + a)

    def substract(self):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b - a)

    def multiply(self):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                self.stack.append(b * a)

    def divide(self):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                if a != 0:
                    self.stack.append(b // a)

    def modulo(self):
        if len(self.stack) >= 2:
            a, b = [self.pop_nb() for _ in range(2)]
            if a != None and b != None:
                if a != 0:
                    self.stack.append(b % a)

    def swap_stack(self):
        if len(self.stack) < 2:
            return
        self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def pop_nb(self):
        return self.stack.pop() if self.stack else None

    def dup_nb(self):
        if len(self.stack) < 1:
            return None
        a = int(self.stack[-1])
        if a != None:
            self.push_nb(a)
    
    def rot_stack(self):
        if len(self.stack) < 3:
            return None
        self.stack.append(self.stack.pop(-3))

    def over_stack(self):
        if len(self.stack) < 2:
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
        tokens = instructions.split()
        while len(tokens):
            token = tokens.pop(0)
            if token == 'DEF':
                self.is_in_def = True
            elif token == 'END':
                self.buffer_to_definition()
                self.is_in_def = False
            else :
                if self.is_in_def:
                    self.def_buffer.append(token)
                    # print("b <----", self.def_buffer, file=sys.stderr, flush=True)
                else:
                    self.rpn.implement_instruction(token)

    def buffer_to_definition(self):
        def_name = self.def_buffer.pop(0)
        tmp = []
        while len(self.def_buffer):
            tmp.append(self.def_buffer.pop(0))
        self.rpn.defs[def_name] = list(tmp)
        print('def', def_name, self.rpn.defs[def_name], file=sys.stderr, flush=True)
        # print("b <----", self.def_buffer, file=sys.stderr, flush=True)


def main():
    input_lines = [ 'DEF MAX OVR OVR SUB POS NOT IF SWP FI POP END',
                    '5 3 MAX 3 7 MAX MAX -2 MAX 4 MAX OUT',
                    '0 1 MAX 13 MAX DUP OUT 20 MAX 7 MAX OUT'
                    ]
    obsolete = ObsoleteProgrammer()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())

