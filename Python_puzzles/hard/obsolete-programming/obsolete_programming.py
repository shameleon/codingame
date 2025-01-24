import sys
import math

""" 50% success - 5 tests 5 validators out of 10 """

import sys
import math

class ObsoleteProgrammer:
    def __init__(self):
        self.stack = []
        self.ops = {'ADD': self.add,
                    'SUB': self.substract,
                    'MUL': self.multiply,
                    'SUB': self.substract,
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
    
    def update_with_input(self, instructions: str):
        self.instructions = instructions.split()
        if self.capture_definition():
            pass
        else:
            self.read_instructions()

    def capture_definition(self):
        line = self.instructions
        if len(line) < 4 or line[0] != 'DEF' or line[-1] != 'END':
            return False
        line.pop()
        line.pop(0)
        def_name = line.pop(0)
        self.defs[def_name] = list(line)
        print('def ', def_name, ":", self.defs[def_name], file=sys.stderr, flush=True)
        return True

    def read_instructions(self) -> None:
        if not self.instructions:
            return None
        instr = self.instructions.pop(0)
        print('------<', instr, file=sys.stderr, flush=True)
        if instr.lstrip('-').isdigit():
            self.stack.append(instr)
        elif instr in self.ops.keys():
            self.ops[instr]()
        elif instr in self.defs.keys():
            self.implement_def(instr)
        print('       ', self.stack, file=sys.stderr, flush=True)
        self.read_instructions()
        return None

    def implement_def(self, func_name: str):
        instructions = self.defs[func_name].copy()
        i = 0
        while len(instructions) > 0:
            instr = instructions.pop(0)
            print ('       ', instr, file=sys.stderr, flush=True)
            if instr.lstrip('-').isdigit():
                self.stack.append(instr)
            elif instr in self.ops.keys():
                self.ops[instr]()
            elif instr == 'IF':
                cond = self.pop_nb()
                conditionnal_instructions = []
                instr2 = ''
                while instr2 != 'FI':
                    instr2 = instructions.pop(0)
                    if cond:
                        conditionnal_instructions.append(instr2)
                    else:
                        pass
                instructions[:] = [*conditionnal_instructions, *instructions]
            print('       ', self.stack, file=sys.stderr, flush=True)  

    def add(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a != None and b != None:
            self.push_nb(a + b)

    def multiply(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a != None and b != None:
            self.push_nb(a * b)

    def substract(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a != None and b != None:
            self.push_nb(b - a)

    def divide(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a != None and b != None and b != 0:
            self.push_nb(b // a)

    def modulo(self):
        a = self.pop_nb()
        b = self.pop_nb()
        if a != None and b != None and b != 0:
            self.push_nb(b % a)

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