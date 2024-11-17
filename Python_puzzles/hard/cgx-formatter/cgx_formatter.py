import sys
import math
import re


class CgxLexerParser:
    def __init__(self, cgx_line):
        self.cgx_line = cgx_line
        self.return_lines = []
        prime = "'hello'= 'pedro'; 'key' = 4'"
        print(self.find_primitive(prime), file=sys.stderr, flush=True)

        self._next_token(cgx_line, 0)

    def is_primitive(self, input_text):
        pattern = re.compile(r'^\'.*\' *= *\'.*\'')
        return pattern.match(input_text)

    def is_boolean(self, input_text):
        pattern = re.compile(r'^true|false', re.IGNORECASE)
        return pattern.match(input_text)

    def find_block(self, line):
        flag = -1
        for i in range(len(line)):
            flag += line[i] == '('
            if line[i] == ')' and flag == 0:
                if i + 2 < len(line):
                    i += line[i + 1] == ';'
                    content = line[:i + 1]
                    return [content, line[i+1:]]
                else:
                    return [line, ""]
            flag -= line[i] == ')'
        return []

    def find_primitive(self, line):
        pattern_key = re.compile(r'^\'.[\']*\' *=')
        end = pattern_key.match(line)
        # key_end = line[1:].find('\'') + 1
        # key = line[:key_end]
        # right_line = line[key_end:].lstrip()
        return line[:end]


    def _print_token(self, token: str, indent: int, next_elem: bool, elem_type='Default'):
        str = (" " * 4 * indent) + token + next_elem * ";"
        endline = '\n'
        print(str, end=endline)

    def _next_token(self, line, indent):
        line = line.strip()
        if line[0] == '(':
            content, next_content = self.find_block(line)
            self._print_token("(", indent, False)
            self._next_token(content, indent + 1)
            self._print_token(")", indent, False)
            self._next_token(next_content, indent)
        elif line[0] == '\'':
            self.find_primitive(line)
        else:
            print(line)


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