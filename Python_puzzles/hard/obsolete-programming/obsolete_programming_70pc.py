import sys


""" 70% success
OK : tests 1:5, 7 validators 1:5, 7, 8 """

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
        """Link pairwise except before an ELSE. then link conditions"""
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
            print('push  >', token, file=sys.stderr, flush=True)
            self.stack.append(int(token))
        elif token in self.ops.keys():
            print('ops   >', token, file=sys.stderr, flush=True)
            self.ops[token]()
        elif token in self.defs.keys():
            print('def   >', token, file=sys.stderr, flush=True)
            self.implement_def(token)
        else:
            return None
        print(' ' * 15, self.stack, file=sys.stderr, flush=True)
        return None
    
    def implement_def(self, def_name: str):
        definition = self.defs[def_name]
        current = definition.instructions[0]
        while current != None:
            if current.token == 'IF':
                top = self.pop_nb()
                print('top stack>', top, file=sys.stderr, flush=True)
                if top != None:
                    current = [current.child_false, current.child_true][top == 1]
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
        into a linked list of instructions"""
        if len(self.def_buffer) > 1:
            new_def = Definition(self.def_buffer)
            self.rpn.defs[new_def.name] = new_def
        print('defs >', self.rpn.defs, file=sys.stderr, flush=True)


def test_6():
    input_lines = [' DEF ABS DUP POS NOT IF 0 SWP SUB FI END ',
                   ' 51 ABS OUT -5 ABS OUT 0 ABS OUT ', ' DEF NZ ',
                   '   OVR ABS OVR ABS SUB ', '   DUP NOT ',
                   '   IF POP DUP POS IF SWP FI ',
                   '   ELS '
                    '     POS IF SWP FI ',
                    '   FI ',
                    '   POP ',
                    ' END ',
                    ' 1 -2 NZ -8 NZ 4 NZ 5 NZ OUT ',
                    ' -12 -5 NZ -137 NZ OUT ',
                    ' 42 -5 NZ 12 NZ 21 NZ 5 NZ 24 NZ OUT ',
                    ' 42 5 NZ 12 NZ 21 NZ -5 NZ 24 NZ OUT ',
                    ' -5 -4 NZ -2 12 NZ NZ -40 4 NZ 2 18 NZ NZ NZ ',
                    ' 11 5 NZ NZ OUT '
                    ]

    """
    ' DEF ABS DUP POS NOT IF 0 SWP SUB FI END '
    ' 51 ABS OUT -5 ABS OUT 0 ABS OUT '
    51
    5
    0
    ' DEF NZ '
    '   OVR ABS OVR ABS SUB '
    '   DUP NOT '
    '   IF POP DUP POS IF SWP FI '
    '   ELS '
    '     POS IF SWP FI '
    '   FI '
    '   POP '
    ' END '
    ' 1 -2 NZ -8 NZ 4 NZ 5 NZ OUT '
    5
    ' -12 -5 NZ -137 NZ OUT '
    -137
    ' 42 -5 NZ 12 NZ 21 NZ 5 NZ 24 NZ OUT '
    24
    ' 42 5 NZ 12 NZ 21 NZ -5 NZ 24 NZ OUT '
    24
    ' -5 -4 NZ -2 12 NZ NZ -40 4 NZ 2 18 NZ NZ NZ '
    ' 11 5 NZ NZ OUT '
    5
                    ]
    """
    return input_lines

def test8():
    input_lines = [' DEF SQ DUP MUL END ',
                    ' DEF PL DUP OUT SQ OUT END ',
                    ' DEF PR OVR PL ',
                    '   SWP 1 ADD OVR OVR SUB POS  ',
                    '   IF SWP PR ELS POP POP FI ',
                    ' END ',
                    ' 1 5 PR ',
                    ' 30 33 PR ']
    return input_lines


def test9():
    """" Hello Fibonacci ! """
    input_lines = [' DEF RFIB DUP  '
                    '   IF 1 SUB ROT ROT DUP ROT ADD ROT RFIB  '
                    '   ELS POP POP FI  '
                    ' END '
                    ' DEF FIB 0 1 ROT RFIB END '
                    ' 5 FIB OUT 6 FIB OUT 2 FIB OUT 10 FIB OUT ']
    return input_lines

def main():

    input_lines = test9()
    obsolete = ObsoleteProgrammer()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())