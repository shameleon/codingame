import sys

""" 100% success """


class Instruction:
    """ A node for definition's indiviual instruction token.
    Only 'IF' token has not-None child_false linked to 'ELS' or 'FI' node"""
    def __init__(self, idx: int, token: str):
        self.idx = idx
        self.token = token
        self.child_true = None
        self.child_false = None

    def __repr__(self):
        res = f'{self.idx} = {self.token} : True {self.child_true}\n'
        if self.child_false != None:
            res += f'{self.idx}.{self.token} False {self.child_false}\n'
        return res


class Definition:
    """ RPN definition instructions are parsed to a linked list"""
    def __init__(self, def_buffer: list):
        self.name = def_buffer.pop(0)
        self.instructions = [Instruction(i, x) for i, x in enumerate(def_buffer)]
        self.index_based_linking_instructions(def_buffer)

    def index_based_linking_instructions(self, def_buffer):
        """Link pairwise except before an ELS. then link conditions"""
        for i, instr in enumerate(self.instructions):
            if i > 0 and instr.token != 'ELS':
                self.instructions[i - 1].child_true = instr
        if_indices = [idx for idx, x in enumerate(def_buffer) if x == 'IF']
        for if_idx in if_indices:
            cond = self.get_condition_indexes(if_idx, def_buffer)
            if cond['ELS'] == None:
                self.link_instructions(cond['IF'], cond['FI'], False)
            else:
                self.link_instructions(cond['IF'], cond['ELS'], False)
                self.link_instructions(cond['ELS'] - 1, cond['FI'], True)

    def get_condition_indexes(self, start_idx, tokens):
        i = start_idx
        k = -1
        cond = dict(zip(['IF', 'ELS', 'FI'], [None] * 3))
        while i < len(tokens):
            if tokens[i] == 'IF':
                if cond['IF'] == None:
                    cond['IF'] = i
                k += 1
            elif tokens[i] == 'ELS':
                if k == 0 and cond['ELS'] == None:
                    cond['ELS'] = i
            elif tokens[i] == 'FI':
                if k == 0 and cond['FI'] == None:
                    cond['FI'] = i
                k -= 1
            i += 1
        return cond
    
    def link_instructions(self, idx1, idx2, child_type=True):
        if child_type:
            self.instructions[idx1].child_true = self.instructions[idx2]
        else:
            self.instructions[idx1].child_false = self.instructions[idx2]

    def __repr__(self):
        res = f'{self.name} : {self.instructions[0]}'
        return res 


class RPN_Calculator:
    """"holds the RPN stack, operations and definitions"""
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
            self.stack.append(int(token))
        elif token in self.ops.keys():
            self.ops[token]()
        elif token in self.defs.keys():
            self.implement_def(token)
        else:
            return None
        return None
    
    def implement_def(self, def_name: str):
        definition = self.defs[def_name]
        current = definition.instructions[0]
        while current != None:
            if current.token == 'IF':
                top = self.pop_nb()
                if top != None:
                    current = [current.child_false, current.child_true][top != 0]
                else:
                    break
            else:
                if current.token != None:
                    self.implement_instruction(current.token)
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
        """Parse tokens, either implement instruction
        or append token to definition buffer until 'END' instruction comes out.
        """
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
                else:
                    self.rpn.implement_instruction(token)

    def buffer_to_definition(self):
        """ upon 'END' instruction, clears definition buffer 
        into a linked list of instructions"""
        if len(self.def_buffer) > 1:
            new_def = Definition(self.def_buffer)
            self.rpn.defs[new_def.name] = new_def
            self.def_buffer.clear()


def test09b():
    input_lines = ['DEF RFIB DUP IF 1 SUB ROT ROT DUP ROT ADD ROT RFIB ELS POP POP FI END',
                    'DEF FIB 0 1 ROT RFIB END',
                    '5 FIB OUT'
    ]
    return input_lines


def test09():
    """" Hello Fibonacci ! """
    input_lines = [' DEF RFIB DUP  '
                    '   IF 1 SUB ROT ROT DUP ROT ADD ROT RFIB  '
                    '   ELS POP POP FI  '
                    ' END '
                    ' DEF FIB 0 1 ROT RFIB END '
                    ' 5 FIB OUT 6 FIB OUT 2 FIB OUT 10 FIB OUT ']
    return input_lines


def main():
    input_lines = test09()
    obsolete = ObsoleteProgrammer()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())