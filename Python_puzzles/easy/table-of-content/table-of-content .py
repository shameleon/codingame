import sys
import math

class Summary:
    def __init__(self):
        self.lenline = int(input())
        self.n =int(input())
        self.entry = [input() for i in range(self.n)]
        self.display_summary()

    def display_summary(self):
        level = [1] * 6
        prev = 0
        for i in range(self.n):
            title, page = self.entry[i].split()
            pure_title = title.lstrip('>')
            indent = len(title) - len(pure_title)
            start = level[indent]
            level[indent] += 1
            level = [1 if i > indent else lvl for i, lvl in enumerate(level)]
            left = ' ' * 4 * indent + str(start) + ' ' + pure_title
            right = str(page)
            dots = '.' * (self.lenline - len(left) - len(right))
            print(left + dots + right)
            prev = indent


if __name__ == "__main__":
    summary = Summary()
