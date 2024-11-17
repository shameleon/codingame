import sys
import math
import re


class CgxQuickFormatter:
    def __init__(self, cgxline):
        self.line  = self.strip_spaces(cgxline)
        print(self.line, file=sys.stderr, flush=True)
        print('-' * 80, file=sys.stderr, flush=True)
        self.parse_line()

    def parse_line(self):
        result = ""
        indent = 0
        inside_string = False
        new_line = True
        previous = None
        for c in self.line:
            if inside_string:
                inside_string =  not (c == '\'')
                result += c
            else:
                if c == '(':
                    if previous == '=':
                        result += '\n' + (indent * ' ')
                    result += (indent * new_line * ' ') + c + '\n'
                    indent += 4
                    new_line = True
                elif c == ')':
                    indent -= 4
                    result += '\n' * (not new_line)
                    result += (indent * ' ') + c
                    new_line = False
                elif c == '\'':
                    result +=  (indent * new_line * ' ') + c
                    inside_string = True
                    new_line = False
                elif c == ';':
                    result += ';\n'
                    new_line = True
                elif c in ['\n', '\t', ' ']:
                    new_line = True
                else:
                    result +=  (indent * new_line * ' ') + c
                    new_line = False
            previous = c
        print(result)

    def strip_spaces(self, line):
        result = ""
        can_strip_space = True
        inside_string = False
        for c in line:
            if inside_string:
                inside_string =  not (c == '\'')
                result += c
            else:
                if c in ['\n', '\t', ' ']:
                    continue
                if c == '\'':
                    inside_string = True
                result += c
        return result
        

def main():
    n = int(input())
    cgxline = ""
    for i in range(n):
        cgxline += input()
    print(f'{cgxline}', file=sys.stderr, flush=True)
    print('-' * 80, file=sys.stderr, flush=True)
    cgx_quick = CgxQuickFormatter(cgxline)
    print('-' * 80, file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()