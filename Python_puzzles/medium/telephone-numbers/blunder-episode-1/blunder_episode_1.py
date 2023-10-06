import sys
import math

""" score 80%"""
class Blunder:
import sys
import math


class Blunder:
    def __init__(self, grid):
        self.priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST']
        self.dir = 'SOUTH'
        self.grid = grid
        self.y, self.x = self.in_grid('@')
        self.breaker = False
        self.inverter = False
        self.teleports = []

    def in_grid(self, target):
        """ Returns the grid coordinates the first
        occurence of a target character in the grid.
        """
        pos = None
        for i, row in enumerate(self.grid):
            for j, c in enumerate(row):
                if c == target:
                    self.grid[i][j] = ' '
                    return i, j
        return 0, 0

    def teleport_blunder(self):
        """ Blunder stepped on a teleporters.
        The other teleport is found and blunder
        is transported there
        """
        x = self.x
        y = self.y
        self.grid[y][x] = 't'
        self.y, self.x = self.in_grid('T')
        self.grid[y][x] = 'T'

    def get_tiles_around(self):
        """ returns a dict of tiles around blunder.
        keys are the four directions possible.
        value is the corresponding grid tile.
        """
        tiles_around = ''
        tiles_around += self.grid[self.y + 1][self.x]
        tiles_around += self.grid[self.y][self.x + 1]
        tiles_around += self.grid[self.y - 1][self.x]
        tiles_around += self.grid[self.y][self.x - 1]
        around = dict(zip(self.priorities, list(tiles_around)))
        return around

    def update_position(self):
        """ Blunder position is updated according to direction taken.
            The direction taken for that step is printed to stdout.
            Blunder move can be breaking a wall 'X'.
            Blunder stepping on teleport 'T' will transport it
            to the other teleport.
        """
        d = self.dir
        if d == 'SOUTH':
            self.y += 1
        elif d == 'NORTH':
            self.y -= 1
        elif d == 'EAST':
            self.x += 1
        elif d == 'WEST':
            self.x -= 1
        print(d)
        if self.grid[self.y][self.x] == 'X':
            self.grid[self.y][self.x] = ' '
        if self.grid[self.y][self.x] == 'T':
            self.teleport_blunder()
        return True

    def change_direction(self):
        """change Blunder direction according to priorities list.
        choosing the next item  in ['SOUTH', 'EAST', 'NORTH', 'WEST'].
        the priority list is reverted after stepping on 'I' tile
        """
        p = self.priorities
        if not self.inverter:
            next_dirs = list(p[1:]) + list(p[:0])
            up_dir = dict(zip(p, next_dirs))
            self.dir = up_dir[self.dir]
        else:
            rev_p = p[::-1]
            next_rev_dir = list(rev_p[1:]) + list(rev_p[:0])
            up_rev_dir = dict(zip(rev_p, next_rev_dir))
            self.dir = up_rev_dir[self.dir]

    def update_move(self):
        """ recursive update of Blunder moves and game parameters"""
        if self.y == 0 or self.x == 0:
            return
        moved = False
        blocked = False
        around = self.get_tiles_around()
        while not moved:
            print("------", self.y , self.x, self.dir, around[self.dir], file=sys.stderr, flush=True)
            next_tile = around[self.dir]
            if next_tile in ['$']:
                print("EXIT !!!", file=sys.stderr, flush=True)
                moved = self.update_position()
            elif next_tile in [' ', '@', 'B', 'I', 'T']:
                if next_tile == 'B':
                    self.breaker = not self.breaker
                elif next_tile == 'I':
                    self.inverter = not self.inverter
                moved = self.update_position()
                self.update_move()
            elif next_tile in ['#', 'X']:
                if self.breaker and next_tile == 'X':
                    moved = self.update_position()
                    self.update_move()
                else:
                    if not blocked:
                        self.dir = 'SOUTH'
                        if self.inverter:
                            self.dir = 'WEST'
                        blocked = True
                    else:
                        self.change_direction()
            elif next_tile in ['E', 'S', 'N', 'W']:
                moved = self.update_position()
                modifier = {'E': 'EAST', 'S': 'SOUTH', 'N': 'NORTH', 'W': 'WEST'}
                self.dir = modifier[next_tile]
                print("--MOD--", self.dir , next_tile, file=sys.stderr, flush=True)
                self.update_move()


if __name__ == "__main__":
    l, c = [int(i) for i in input().split()]
    grid = []
    for i in range(l):
        row = list(input())
        print(*row, file=sys.stderr, flush=True)
        grid.append(row)
    robot = Blunder(grid)
    robot.update_move()


    def __init__(self, grid):
        self.priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST']
        self.dir = 'SOUTH'
        self.grid = grid
        self.y, self.x = self.in_grid('@')
        self.breaker = False
        self.inverter = False
        self.teleports = []

    def in_grid(self, target):
        """ Returns the grid coordinates the first
        occurence of a target character in the grid.
        """
        pos = None
        for i, row in enumerate(self.grid):
            for j, c in enumerate(row):
                if c == target:
                    self.grid[i][j] = ' '
                    return i, j
        return 0, 0

    def teleport_blunder(self):
        """ Blunder stepped on a teleporters.
        The other teleport is found and blunder
        is transported there
        """
        x = self.x
        y = self.y
        self.grid[y][x] = 't'
        self.y, self.x = self.in_grid('T')
        self.grid[y][x] = 'T'

    def get_tiles_around(self):
        """ returns a dict of tiles around blunder.
        keys are the four directions possible.
        value is the corresponding grid tile.
        """
        tiles_around = ''
        tiles_around += self.grid[self.y + 1][self.x]
        tiles_around += self.grid[self.y][self.x + 1]
        tiles_around += self.grid[self.y - 1][self.x]
        tiles_around += self.grid[self.y][self.x - 1]
        around = dict(zip(self.priorities, list(tiles_around)))
        return around

    def update_position(self):
        """ Blunder position is updated according to direction taken.
            The direction taken for that step is printed to stdout.
            Blunder move can be breaking a wall 'X'.
            Blunder stepping on teleport 'T' will transport it
            to the other teleport.
        """
        d = self.dir
        if d == 'SOUTH':
            self.y += 1
        elif d == 'NORTH':
            self.y -= 1
        elif d == 'EAST':
            self.x += 1
        elif d == 'WEST':
            self.x -= 1
        print(d)
        if self.grid[self.y][self.x] == 'X':
            self.grid[self.y][self.x] = ' '
        if self.grid[self.y][self.x] == 'T':
            self.teleport_blunder()
        return True

    def change_direction(self):
        """change Blunder direction according to priorities list.
        choosing the next item  in ['SOUTH', 'EAST', 'NORTH', 'WEST'].
        the priority list is reverted after stepping on 'I' tile
        """
        p = self.priorities
        if not self.inverter:
            next_dirs = list(p[1:]) + list(p[:0])
            up_dir = dict(zip(p, next_dirs))
            self.dir = up_dir[self.dir]
        else:
            rev_p = p[::-1]
            next_rev_dir = list(rev_p[1:]) + list(rev_p[:0])
            up_rev_dir = dict(zip(rev_p, next_rev_dir))
            self.dir = up_rev_dir[self.dir]

    def update_move(self):
        """ recursive update of Blunder moves and game parameters"""
        if self.y == 0 or self.x == 0:
            return
        moved = False
        blocked = False
        around = self.get_tiles_around()
        while not moved:
            print("------", self.y , self.x, self.dir, around[self.dir], file=sys.stderr, flush=True)
            next_tile = around[self.dir]
            if next_tile in ['$']:
                print("EXIT !!!", file=sys.stderr, flush=True)
                moved = self.update_position()
            elif next_tile in [' ', '@', 'B', 'I', 'T']:
                if next_tile == 'B':
                    self.breaker = not self.breaker
                elif next_tile == 'I':
                    self.inverter = not self.inverter
                moved = self.update_position()
                self.update_move()
            elif next_tile in ['#', 'X']:
                if self.breaker and next_tile == 'X':
                    moved = self.update_position()
                    self.update_move()
                else:
                    if not blocked:
                        self.dir = 'SOUTH'
                        if self.inverter:
                            self.dir = 'WEST'
                        blocked = True
                    else:
                        self.change_direction()
            elif next_tile in ['E', 'S', 'N', 'W']:
                moved = self.update_position()
                modifier = {'E': 'EAST', 'S': 'SOUTH', 'N': 'NORTH', 'W': 'WEST'}
                self.dir = modifier[next_tile]
                print("--MOD--", self.dir , next_tile, file=sys.stderr, flush=True)
                self.update_move()


if __name__ == "__main__":
    l, c = [int(i) for i in input().split()]
    grid = []
    for i in range(l):
        row = list(input())
        print(*row, file=sys.stderr, flush=True)
        grid.append(row)
    robot = Blunder(grid)
    robot.update_move()

