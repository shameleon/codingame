import sys
import math

class Map:
    def __init__(self, map, h, w):
        self.map = map
        self.h = h
        self.w = w

class PlaceInGrid:
    def __init__(self):
        self.solutions = []
        self.count = 0

    def create_object(self, obj, a, b):
        self.object = Map(obj, a, b)
    
    def create_grid(self, grid, c, d):
        self.grid = Map(grid, c, d)

    def find_all_solutions(self):
        for i in range(self.grid.h - self.object.h + 1):
            for j in range(self.grid.w - self.object.w + 1):
                print("i", i, "j", j, file=sys.stderr, flush=True)
                self._is_it_a_solution(i, j)

    def _is_it_a_solution(self, i, j):
        obj = self.object.map
        grid = self.grid.map
        a = self.object.h
        b = self.object.w
        d = self.grid.w
        line = 0
        while line < a:
            if not obj_line_fits(obj[line], grid[i + line][j:j + b]):
                return False
            line += 1
        self.solutions.append([i, j])
        self.count += 1
        return True

    def _print_inserted_line(self, grid_line, obj_line, sol_w):
        print(grid_line, obj_line, file=sys.stderr, flush=True)
        for j in range(self.object.w):
            x = sol_w + j
            if grid_line[x] == '.' and obj_line[j] == '*':
                grid_line = grid_line[:x] + '*' + grid_line[x + 1:] 
        print(grid_line)

    def display_unique_solution(self):
        if self.count != 1:
            return
        sol_h, sol_w = self.solutions[0]
        obj_y = 0
        for i in range(self.grid.h):
            if i >= sol_h and i < sol_h + self.object.h:
                print("i", i, obj_y, sol_w, file=sys.stderr, flush=True)
                self._print_inserted_line(self.grid.map[i], self.object.map[obj_y], sol_w)
                obj_y += 1
            else:
                print(self.grid.map[i])  


def obj_line_fits(obj_line, grid_line):
    if len(obj_line) != len(grid_line):
        return False
    for i in range(len(obj_line)):
        if obj_line[i] == '*' and grid_line[i] == '#':
            return False
    print("fits", file=sys.stderr, flush=True)
    return True 


def main():
    a, b = [int(i) for i in input().split()]
    print(a, b, file=sys.stderr, flush=True)
    obj = []
    for i in range(a):
        obj.append(input())
        print(obj[i], file=sys.stderr, flush=True)
    print("-" * 20, file=sys.stderr, flush=True)
    c, d = [int(i) for i in input().split()]
    print(c, d, file=sys.stderr, flush=True)
    grid = []
    solutions = []
    for i in range(c):
        grid.append(input())
        print(grid[i], file=sys.stderr, flush=True)
    print(grid, file=sys.stderr, flush=True)

    grid_insert = PlaceInGrid()
    grid_insert.create_object(obj, a, b)
    grid_insert.create_grid(grid, c, d)
    grid_insert.find_all_solutions()
    print(grid_insert.count)
    grid_insert.display_unique_solution()


if __name__ == "__main__":
    main()
