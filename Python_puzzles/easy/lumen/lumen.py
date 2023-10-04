import sys
import math

class LightArray:
    def __init__(self, n, l):
        self.arr = [[0 for i in range(n)] for j in range(n)]
        self.n = n
        self.l = l
        self.nb_dark_cells = n * n
    
    def place_candle(self, r, c):
        self.arr[r][c] = self.l
        self.update(r, c)

    def update(self, r, c):
        for i in range(self.n):
            for j in range(self.n):
                dist =  max(abs(i - r), abs(j -c))
                if (dist < self.l):
                    self.arr[i][j] = self.l - dist

    def get_dark_cells(self):
        nb_dark_cells = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.arr[i][j] == 0:
                    nb_dark_cells += 1
        print(nb_dark_cells)


def main():
    n = int(input())
    l = int(input())
    grid = [[" "] * n] * n
    light_in_arr = LightArray(n, l)
    for i in range(n):
        grid[i] = input().split(" ")
        for j in range(n):
            if grid[i][j] == "C":
                light_in_arr.place_candle(i, j)
    print(grid, file=sys.stderr, flush=True)
    light_in_arr.get_dark_cells()


if __name__ == "__main__":
    main()