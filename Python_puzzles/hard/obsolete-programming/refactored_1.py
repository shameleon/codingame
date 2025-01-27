import sys

class Instruction:
    def __init__(self, token):
        self.token = token
        self.is_if_fork = False
        self.child_true = None
        self.child_false = None
        self.is_end = False
        self.is_true_branch = True

    def add_child(self, instr_true):
        if not instr_true:
            instr_true = 'END'
        self.child_true = Instruction(instr_true)
        print(f'child to {self.token} : true {self.child_true.token}', file=sys.stderr, flush=True)
    
    def add_else_child_to_if(self, instr_false):
        self.child_false = Instruction(instr_false)
        print(f'child to {self.token} : true {self.child_true.token}', file=sys.stderr, flush=True)

    def __repr__(self):
        return f'{self.token} T-> {self.child_true} F-> {self.child_false}\n'


class Definition:
    def __init__(self, def_buffer: list):
        self.name = def_buffer.pop(0)
        self.if_fork = None
        self.end_of_true_branch = None
        self.is_true_branch = True
        self.head = Instruction(def_buffer.pop(0))
        self.parse_buffer(self.head, def_buffer)

    def parse_buffer(self, current, def_buffer):
        if len(def_buffer) == 0:
            current.add_child('END')
            return
        next_token = def_buffer.pop(0)
        if next_token == 'ELSE':
            self.is_true_branch = False
            next_token  = def_buffer.pop(0)
            self.if_fork.add_else_child_to_if(next_token)
            self.end_of_true_branch = current
            current = self.if_fork.child_false
            self.parse_buffer(current.child_false, def_buffer)
            return
        elif next_token == 'FI':
            if self.is_true_branch:
                current.add_child(def_buffer.pop(0))
            else:
                self.end_of_true_branch.add_child(def_buffer.pop(0))
                current.child_true = self.end_of_true_branch.child_true
        else:
            current.add_child(next_token)
            if next_token == 'IF':
                self.if_fork = current.child_true
                self.is_if_fork = True    ## remove ?
        self.parse_buffer(current.child_true, def_buffer)


    def __repr__(self):
        res = f'{self.name} :\n'
        current = self.head
        while current:
            res += f'{current}'
            current = current.child_true
            return res
        

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
            # self.if_else_buffer.append(token)
            # pop the top if true pick child accordingly
            pass
        else:
            return None
        print('             ', self.stack, file=sys.stderr, flush=True)
        return None
    
    def implement_def(self, def_name: str):
        definition = self.defs[def_name]
        current = definition.head
        while current != None:
            self.implement_instruction(current.token)
            ## what if child false
            current = current.child_true
            
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
        """Parse tokens, either implementing instruction
        or appending it to definition buffer until 'END' instruction comes out.
        """
        tokens = instructions.split()
        while len(tokens):
            token = tokens.pop(0)
            if token == 'DEF':
                self.is_in_def = True
            elif token == 'END':
                print('def_buffer >', self.def_buffer, file=sys.stderr, flush=True)
                self.buffer_to_definition()
                self.is_in_def = False
            else :
                if self.is_in_def:
                    self.def_buffer.append(token)
                else:
                    self.rpn.implement_instruction(token)

    def buffer_to_definition(self):
        """ upon 'END' instruction, empties definition buffer 
        into a chained list of instructions"""
        if len(self.def_buffer) > 1:
            new_def = Definition(self.def_buffer)
            self.rpn.defs[new_def.name] = new_def
        print('defs >', self.rpn.defs, file=sys.stderr, flush=True)



def main():
    input_lines = [ 'DEF PIZ OVR SUB POS IF ADD MOD ELSE MUL SUB FI SWP OUT',
                   'END',
                   '1 2 3 4 5 6 PIZ PIZ PIZ'
                   ]
    obsolete = ObsoleteProgrammer()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())



