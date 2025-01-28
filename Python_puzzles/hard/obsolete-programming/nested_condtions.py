import sys



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