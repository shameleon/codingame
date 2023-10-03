import sys
import math

class Node:
    def __init__(self, digit, parent=None):
        self.level = 0
        self.digit = digit
        self.parent = parent
        self.children = []
    
    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children)

    def depth(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.depth() + 1

    def search_children(self, digit):
        for child in self.children:
            if child.digit == digit:
                return child
        return None 


class Phonebook:
    def __init__(self, n):
        self.n = n
        self.roots = []
        self.nodes = []

    def search_roots(self, digit):
        for root in self.roots:
            if root.digit == digit:
                return root
        return None

    def add_number(self, nbr):
        print(nbr, file=sys.stderr, flush=True)
        root = self.search_roots(nbr[0])
        if root == None:
            root = Node(nbr[0])
            self.roots.append(root)
            self.nodes.append(root)
        print("h>", root.digit, end='', file=sys.stderr, flush=True)
        current = root
        for dig in nbr[1:]:
            child = current.search_children(dig)
            if child == None:
                child = Node(dig, current)
                current.children.append(child)
                self.nodes.append(child)
            print(" >", child.digit, end='', file=sys.stderr, flush=True)
            current = child
        if current.is_leaf() == 0:
            print(" -leaf", current.depth() + 1, end='', file=sys.stderr, flush=True)


    def count_elements(self):
        return len(self.nodes)


def main():
    n = int(input())
    phone = Phonebook(n)
    for i in range(n):
        phone_number = input()
        # print(phone_number, file=sys.stderr, flush=True)
        phone.add_number(phone_number)
    print(phone.count_elements())


if __name__ == "__main__":
    main()
