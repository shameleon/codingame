import sys
import math


class Mountain:
    def __init__(self, height: int):
        self.h = height
        self.mid = height

    def get_line(self, y):
        lst = [" "] * self.mid * 2
        mid = self.mid
        if y <= self.h:
            left = (mid - 1) - (self.h - y)
            right = mid + (self.h - y)
            lst[left]= "/"
            lst[right]= '\\'
        return "".join(lst)


class MountainMap:
    def __init__(self, n, heights):
        self.n = n
        self.heights = [int(h) for h in heights]
        self.h_max = max(self.heights)
        self.mountains = [Mountain(int(h)) for h in heights]
        print(*[h for h in self.heights], file=sys.stderr, flush=True)

    def print_map(self):
        for y in range(self.h_max, 0, -1):
            line = ""
            for mountain in self.mountains:
                line += mountain.get_line(y)
            print(line.rstrip())


def main():
    n = int(input())
    m_map = MountainMap(n, input().split())
    m_map.print_map()


if __name__ == "__main__":
    main()
