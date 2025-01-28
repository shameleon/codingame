import sys

class Instruction:
    def __init__(self, token):
        self.token = token

class Definition:
    def __init__(self, def_buffer: list):
        self.name = def_buffer.pop(0)
        self.splice_conditions(def_buffer)

    def splice_conditions(self, tokens):
        # for i, token in enumerate(instructions):
        # first_if = tokens.index('IF', 0, len(tokens))
        i = 0
        k = -1
        cond = [None] * 3
        while i < len(tokens):
            if tokens[i] == 'IF':
                if cond[0] == None:
                    cond[0] = i
                    k += 1
                else:
                    k += 1
            elif tokens[i] == 'ELSE':
                if k == 0 and cond[1] == None:
                    cond[1] = i
            elif tokens[i] == 'FI':
                if k == 0 and cond[2] == None:
                    cond[2] = i
                else:
                    k -= 1
            i += 1
            a, b, c = cond
        if b:
            print(tokens[a:b], tokens[b:c])
        else:
            print(tokens[a:c])
    
    def __repr__(self):
        res = f'{self.name} :\n'
        return res


class TestInstructionsClass:
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
        print('defs >', self.defs, file=sys.stderr, flush=True)


def main():
    input_lines_0 = [ 'DEF MAX OVR OVR SUB POS NOT IF',
                    'SWP FI POP END',
                    '5 3 MAX 3 7 MAX MAX -2 MAX 4 MAX OUT',
                    '0 1 MAX 13 MAX DUP OUT 20 MAX 7 MAX OUT'
                    ]
    
    #                         0   1  2   3   4  5   6    7   8   9  0   11   12  13 14  15
    input_lines = [ 'DEF MAX OVR IF OVR IF MUL DIV ELSE TOP DUP FI IF TOP ELSE DUP FI ADD SWP ELSE DUP NOT  IF TOP FI IF TOP ELSE DUP FI TOP FI SWP POP END']
    obsolete = TestInstructionsClass()
    for line in input_lines:
        obsolete.update_with_input(line)


if __name__ == '__main__':
    sys.exit(main())