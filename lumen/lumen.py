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

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
l = int(input())
grid = [[" "] * n] * n
light_in_arr = LightArray(n, l)
for i in range(n):
    grid[i] = input().split(" ")
    for j in range(n):
        if grid[i][j] == "C":
            light_in_arr.place_candle(i, j)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(grid, file=sys.stderr, flush=True)
light_in_arr.get_dark_cells()

# grid =[]
# for x in range(n):
#    grid +=[[l if c=='C' else 0 for c in input().split()]]
