import sys
import math
import re

""" 
https://regexr.com/
https://www.programiz.com/python-programming/regex
https://ruslanspivak.com/lsbasi-part7/
"""
"""
        rules = {'Bool_val': re.compile(r'(true|false){1}\;{0,1}'),
                 'Num_val': re.compile(r'\-?\d+(\.\d+)?'),
                 'Primitive': re.compile(r'\'(.[^\'])+\''),
                 'Key': re.compile(r'\'\w+\'=')
                 'Key-Value': re.compile(r'')}
"""


class CgxLexerParser:
    def __init__(self, line):
        self.line = line
        self.root = Node('Root', line)
        self.nodes = []
        self.lexer(self.root, line)

    def rules(self):
        dict 

    def lexer(self, line):
        b = 0
        if line[b] == '(':
            pass

    def _is_primitive(self, line):
        if line[0] == '\'':
           for c in line[1:-1]:
                pass

def main():
    n = int(input())
    cgxline = ""
    for i in range(n):
        cgxline += input()
    print(f'{cgxline}$', file=sys.stderr, flush=True)
    parsing = CgxLexerParser(cgxline)


if __name__ == "__main__":
    main()