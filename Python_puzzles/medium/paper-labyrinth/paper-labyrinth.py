import sys


class Cell:
    def __init__(self, i: int, j: int, walls: str):
        self.i = i
        self.j = j
        self.walls = [(wall) == '1' for wall in walls]
        self.is_start = False
        self.is_rabbit = False
        self.neighbors_coord = self.get_neighbor_coordinates()
        self.level = None
        self.back = None
        self.children = []

    def get_neighbor_coordinates(self):
        moves = {'R': (0, 1), 'T': (-1, 0), 'L': (0, -1), 'D': (1, 0)}
        dirs = ['R', 'T', 'L', 'D']
        neighbors = []
        for k in range(4):
            if not self.walls[k]:
                coord = moves[dirs[k]]
                other_i = self.i + coord[0]
                other_j = self.j + coord[1]
                neighbors.append(tuple([other_i, other_j]))
        return neighbors

    def update_level(self, score):
        if self.level and self.level < score:
            return
        self.level = score

    def update_backwards(self, score):
        if self.back and self.back < score:
            return
        self.back = score

    def get_coord(self):
        return tuple([self.i, self.j])

    def __repr__(self):
        return f'{self.i} , {self.j} : {self.walls}' \
            + f' {(self.is_start) * " is start"}' \
            + f' {(self.is_rabbit) * "is rabbit"}' \
            + f' {self.neighbors_coord}'


class Labyrinth:
    def __init__(self):
        start_end = [int(i) for i in input().split()]
        rabbit = [int(i) for i in input().split()]
        self.w, self.h = [int(i) for i in input().split()]
        self.arr = [input() for i in range(self.h)]
        print(*self.arr, file=sys.stderr, flush=True)
        self.cells = []
        self.create_cells(start_end, rabbit)
        for cell in self.cells:
            print(cell, file=sys.stderr, flush=True)
        self.scores = []
        self.go_to_rabbit(self.entrance, 0)
        cells_to_reach_rabbit = min(self.scores)
        self.way_back = []
        self.go_to_exit(self.rabbit, 0)
        print(cells_to_reach_rabbit, min(self.way_back))

    def create_cells(self, start_end, rabbit):
        for i in range(self.h):
            for j in range(self.w):
                walls = format(int(self.arr[i][j], 16), '0>4b')
                cell = Cell(i, j, walls)
                self.cells.append(cell)
                if i == start_end[1] and j == start_end[0]:
                    cell.is_start = True
                    self.entrance = cell
                elif i == rabbit[1] and j == rabbit[0]:
                    cell.is_rabbit = True
                    self.rabbit = cell
    
    def go_to_rabbit(self, current, score):
        current.update_level(score)
        if current.is_rabbit:
            self.scores.append(score)
            return
        elif current.is_start and score != 0:
            return
        for coord in current.neighbors_coord:
            for cell in self.cells:
                if cell.get_coord() == coord:
                    if not cell.level or current.level < cell.level:                    
                        current.children.append(cell)
                        self.go_to_rabbit(cell, score + 1)

    def go_to_exit(self, current, score):
        current.update_backwards(score)
        if current.is_start:
            self.way_back.append(score)
            return
        elif current.is_rabbit and score != 0:
            return
        for coord in current.neighbors_coord:
            for cell in self.cells:
                if cell.get_coord() == coord:
                    if not cell.back or current.back < cell.back:                    
                        self.go_to_exit(cell, score + 1)   


def main():
    Labyrinth()


if __name__ == '__main__':
    sys.exit(main())
