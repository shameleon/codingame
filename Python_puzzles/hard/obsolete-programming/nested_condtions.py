import sys


class Instruction:
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
    def __init__(self, def_buffer: list):
        self.name = def_buffer.pop(0)
        self.instructions = [Instruction(i, x) for i, x in enumerate(def_buffer)]
        self.index_based_linking_instructions(def_buffer)

    def index_based_linking_instructions(self, def_buffer):
        """Link pairwise except before an ELSE. then link conditions"""
        for i, instr in enumerate(self.instructions):
            if i > 0 and  instr.token != 'ELSE':
                self.instructions[i - 1].child_true = instr
        if_indexes = [idx for idx, x in enumerate(def_buffer) if x == 'IF']
        for if_idx in if_indexes:
            cond = self.get_condition_indexes(if_idx, def_buffer)
            if cond['ELSE'] == None:
                self.link_instructions(cond['IF'], cond['FI'], False)
            else:
                self.link_instructions(cond['IF'], cond['ELSE'], False)
                self.link_instructions(cond['ELSE'] - 1, cond['FI'], True)

    def get_condition_indexes(self, start_idx, tokens):
        i = start_idx
        k = -1
        cond = dict(zip(['IF', 'ELSE', 'FI'], [None] * 3))
        while i < len(tokens):
            if tokens[i] == 'IF':
                if cond['IF'] == None:
                    cond['IF'] = i
                k += 1
            elif tokens[i] == 'ELSE':
                if k == 0 and cond['ELSE'] == None:
                    cond['ELSE'] = i
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


class TestDefinitonClass:
    def __init__(self):
        #self.rpn = RPN_Calculator()
        self.def_buffer = []
        self.is_in_def = False
        self.defs = {}

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
                else:
                    #self.rpn.implement_instruction(token)
                    pass

    def buffer_to_definition(self):
        """ upon 'END' instruction, empties definition buffer 
        into a chained list of instructions"""
        if len(self.def_buffer) > 1:
            new_def = Definition(self.def_buffer)
            self.defs[new_def.name] = new_def
        print('def >', new_def, file=sys.stderr, flush=True)


def main():
    input_lines_0 = [ 'DEF MAX OVR OVR SUB POS NOT IF',
                    'SWP FI POP END',
                    '5 3 MAX 3 7 MAX MAX -2 MAX 4 MAX OUT',
                    '0 1 MAX 13 MAX DUP OUT 20 MAX 7 MAX OUT'
                    ]
    
    #                         0   1  2   3   4  5   6    7   8   9  0   11   12  13 14  15 16
    input_lines = [ 'DEF MAX OVR IF OVR IF MUL DIV ELSE TOP DUP FI NOT ELSE DUP TOP FI SWP POP END']
    obsolete = TestDefinitonClass()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())