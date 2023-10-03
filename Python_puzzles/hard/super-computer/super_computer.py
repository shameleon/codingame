import sys
import math

"""
class Leaf:
    def __init__(self, key: tuple):
        self.child = []
        self.key = key
        self.leaf = False
    
    def __str__(self):
        return f'{self.key[0]}-{self.key[1]}'


class BTree:
    def __init__(self, n):
        self.nb_leaves = n
        self.root = Leaf((0, 0))

    def insert(self, key: tuple):
        leaf = Leaf(key)
        root = self.root
        if not root.leaf:
            self.root.child.append(leaf)
            self.root.leaf = True
        else next = self.root.child.
"""



class CalcPlanner:
    def __init__(self, n):
        self.reservations = [] 
        self.denied = []

    def find_dates(self):
        self.reservations.sort(key=lambda x : x[1])
        max = self.reservations[-1][1]
        print("max =", max, file=sys.stderr, flush=True)
        for calc in self.reservations[:40]:
            print(calc[0], calc[1], file=sys.stderr, flush=True)

    def push(self, j, d):
        begin = j
        end = j + d - 1
        self.reservations.append((begin, end))

    def __str__(self):
        return str(len(self.reservations))

def main():
    n = int(input())
    cal = CalcPlanner(n)
    print("n =", n, file=sys.stderr, flush=True)
    for i in range(n):
        j, d = [int(j) for j in input().split()]
        cal.push(j, d)
    cal.find_dates()
    print(cal)

if __name__ == "__main__":
    main()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

