import sys
import math


class ReverseMining:
    def __init__(self, w, h, grid):
        self.w = w
        self.h = h
        self.grid = grid
        self.result_grid = []

    def find_neighbors(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.grid[i][j] != 'x':
                    self.set_cell_value(i, j)
            line = ''.join(self.grid[i])
            result_line = line.replace("x", ".")
            self.result_grid.append(result_line)
            print(result_line)


    def set_cell_value(self, i, j):
        count_mines = 0
        for y in [i - 1, i, i + 1]:
            if y >= 0 and y < self.h:
                for x in [j - 1, j, j+ 1]:
                    if x >= 0 and x < self.w:
                        if self.grid[y][x] == 'x':
                            count_mines += 1
        if count_mines > 0:
            self.grid[i][j] = str(count_mines)


def main():
    w = int(input())
    h = int(input())
    print(w, h, file=sys.stderr, flush=True)
    grid = []
    for i in range(h):
        line = list(input())
        grid.append(line)
    reverse_mining = ReverseMining(w, h, grid)
    reverse_mining.find_neighbors()
    

if __name__ == "__main__":
    main()