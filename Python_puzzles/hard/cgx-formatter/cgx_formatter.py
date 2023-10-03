import sys
import math
import re

""" 
https://regexr.com/
https://www.programiz.com/python-programming/regex
https://ruslanspivak.com/lsbasi-part7/
"""

class Node:
    def __init__(self, element_type, content, indent):
        self.type = element_type
        self.content = content
        self.indent = indent
        self.childs = []

class CgxLexerParser:
    def __init__(self, line):
        self.line = line
        self.ast_tree = []
        self.ast_tree.append(Node('root', None, -1))
        self.return_lines = []
        # self.identify_element(line, 0)
        self._next_token(line, 0)

    
    def _print_token(self, token: str, indent: int, next_elem: bool, elem_type='Default'):
        str = (" " * 4 * indent) + token + next_elem * ";"
        endline = '\n'
        print(str, end=endline)

    def _next_token(self, line, indent):
        """ lexer
        3 types of elements : 'Block' 'Value' 'Primitive'"""
        if len(line) == 0:
            return
        next_elem = (line[-1] == ';')
        if next_elem:
            line = line[0:-2]
        many_values = re.search(r'(\'?\-?\w+\'?\;)+(\'?\-?\w+\'?)$', line)
        if many_values:
            found_values = re.search(r'\'?\-?\w+\'?;', line)
            last = re.search(r'(\'?\-?\w+\'?)$', line)
            if found_values and last:
                values = re.finditer(r'\'?\-?\w+\'?;', line)
                for value in values:
                    self._print_token(value.group(), indent, False)
                    #print(value.group(), file=sys.stderr, flush=True)
                    #self._next_token(value.group(), indent)
                #print(last.group(), file=sys.stderr, flush=True)
                self._print_token(last.group(), indent, False)
                #self._next_token(last.group(), indent)
        elif line[0] == '(' and line[-1] == ')':
            content = line[1: -1]
            self._print_token("(", indent, next_elem)
            self._next_token(line[1: -1], indent + 1)
            self._print_token(")", indent, next_elem)
        elif line[0] == '\'' and line[-1] == '\'':
            self._print_token(line, indent, next_elem)
        else:
            print("VALUE", file=sys.stderr, flush=True)
            bool_val = re.search(r'true|false', line)
            num_val = re.search(r'^\-?\d+$', line)
            if bool_val:
                self._print_token(bool_val.group(), indent, next_elem)
            elif num_val:
                self._print_token(num_val.group(), indent, next_elem)


        """
        Do a regex search against all defined regexes and
        return the key and match result of the first matching regex

        r'\'?\-?\w+\''  matches to -42, 42, 'toto' 'titi42'
        ^\((\-?\d)+(\;{1}\-?\d+)*\)$ (-250;-354545;-514352;1353135)

       cgx_dict = {'Value': re.compile(r'\w[^();]{2,15}'),
                   'key': re.compile(r'\'\w[^();]{2,15}\''),
                   'Primitive': re.compile(r'\'\w[^();]{2,200}\''),
                   'Block': re.compile(r'^\(.\($')}
        cgx_dict = {'boolean': re.compile(r'true')}
        # print(f'{indent}-level', file=sys.stderr, flush=True)
        #for key, rx_cgx in cgx_dict.items():
        # re.search(r'^(\-?\d+)(\;{1}\-?\d+)*$', line):
        # match4 = re.search(r'^(\-?\d+)(\;{1}\-?\d+)*$', line)
        # match1 = re.search(r'true|false', line)
        # match6 = re.search(r'^\-?\d{1,15}\;?', line)
        # if match4:
        #     s4 = match4.group()
        #     s4sub = re.sub(';', '; ', s4[1:-1])
        #     s4splt = s4sub.split(' ')
        #     for s in s4splt:
        #         self._print_token(indent, line)
        # # bool value
        # elif match1:
        #     self._print_token(indent, match1.group())
        # elif match6:
        #     self._print_token(indent, match6.group())
        # primitive
        # match2 = re.search(r'\'.[^();=]{2,200}\'', line)

        # match3 = re.search(r'\((.+[^;])+.+\)', line)
        # if match3:
        #     s3 = match3.group()
        #     print("(")
        #     print("   ", s3[1:-1])
        #     print(")")
        # match4 = re.search(r'^\((\-?\d+)(\;{1}\-?\d+)*\)$', line)
        # value
        # match4 = re.search(r'^(\-?\d+)(\;{1}\-?\d+)*$', line)
        # if match4:
        #     s4 = match4.group()
        #     s4sub = re.sub(';', '; ', s4[1:-1])
        #     s4splt = s4sub.split(' ')
        #     for s in s4splt:
        #         print(" " * (4 * indent - 1), s)
        """

def main():
    n = int(input())
    cgxline = ""
    for i in range(n):
        cgxline += input()
    print(f'{cgxline}$', file=sys.stderr, flush=True)
    parsing = CgxLexerParser(cgxline)


if __name__ == "__main__":
    main()