import sys
import math
import re



class Node:
    """ stores elements """
    def __init__(self, content, parent=None, element_type=None):
        self.type = element_type
        self.content = content
        self.parent = parent
        self.colon = False
        self.children = []
        self.depth = self.depth()
        self.check_content()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children)

    def depth(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.depth() + 1
        
    def check_content(self):
        line = self.line
        if line[-1] == ';':
            self.colon = True
            line = line[0:-1]
        if self.line[0] == '(' and self.line[-1] == ')':
            
            for c in line:
                c == '(':
                    +=
            
        # rules = {'Bool_val': re.compile(r'(true|false){1}\;{0,1}'),
        #          'Num_val': re.compile(r'\-?\d+(\.\d+)?'),
        #          'Primitive': re.compile(r'\'(.[^\'])+\''),
        #          'Key': re.compile(r'\'\w+\'='),
        #          'Key-Value': re.compile(r'')}
        # if self.type != None:
        #     return
        # for key, rule in rules.items():
        #     m = re.fullmatch(rule, self.content)
        #     m.span()
    
    def print_children(self):


class CgxLexerParser:
    def __init__(self, line):
        self.line = line
        self.root = []
        self.nodes = []
        self.lexer(self.root, line)

    def lexer(self, parent, line):
        line = line.lstrip()
        line = line.rstrip()
        if len(line) == 0:
            return
        self.root.append(Node(line))

    def print_tokens(self):
        for root in self.root:
            root.print_children()

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


def main():
    n = int(input())
    cgxline = ""
    for i in range(n):
        cgxline += input()
    print(f'{cgxline}$', file=sys.stderr, flush=True)
    parsing = CgxLexerParser(cgxline)


if __name__ == "__main__":
    main()