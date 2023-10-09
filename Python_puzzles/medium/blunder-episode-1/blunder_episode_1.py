import sys
import math

""" progress : 91% """


class State:
    def __init__(self, grid):
        self.grid = grid
        self.states = []
        self.idx = []
        self.threshold = 1

    def save(self, status):
        found = False
        s = "(" + str(status[0]) + "-" + str(status[1]) + ")"
        s += str(status[2:5]) 
        for i, st in enumerate(self.states):
            if s == st:
                self.idx.append(i)
                found = True
        if not found:
            self.states.append(s)
        return self._loop_detected()

    def _loop_detected(self):
        repeats = 0
        if len(self.idx) >= 10:
            keys = []
            counter = []
            for i in self.idx:
                if i not in keys:
                    keys.append(i)
                    repeats = self.idx.count(i)
                    counter.append(repeats)
                    if repeats > self.threshold:
                        print(counter, repeats, file=sys.stderr, flush=True)
                        return True
        return False


class Blunder:
    def __init__(self, grid):
        self.priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST']
        self.dir = 'SOUTH'
        self.grid = grid
        self.y, self.x = self.in_grid('@')
        self.breaker = False
        self.inverter = False
        self.state = State(grid)
        self.loop_detected = False

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

    def print_grid(self):
        for row in self.grid:
            print(*row, file=sys.stderr, flush=True)

    def get_present_state(self):
        return list([self.x, self.y, self.breaker, self.inverter, self.dir])

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
        print([d, 'LOOP'][self.loop_detected])
        if self.grid[self.y][self.x] == 'X':
            self.grid[self.y][self.x] = ' '
        elif self.grid[self.y][self.x] == 'T':
            self.teleport_blunder()
        return True

    def change_direction(self):
        """ Blunder direction changes according to priorities list.
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
        self.loop_detected = self.state.save(self.get_present_state()) 

    def update_move(self):
        """ recursive update of Blunder moves and game parameters"""
        if self.y == 0 or self.x == 0:
            return
        moved = False
        blocked = False
        around = self.get_tiles_around()
        while not moved:
            next_tile = around[self.dir]
            if next_tile in ['$'] or self.loop_detected:
                # print("EXIT !!!", file=sys.stderr, flush=True)
                moved = self.update_position()
            elif next_tile in [' ', '@', 'B', 'I', 'T']:
                if next_tile == 'B':
                    self.breaker = not self.breaker
                    # print("BBBBB", ['sober', 'breaker'][self.breaker] , file=sys.stderr, flush=True)
                elif next_tile == 'I':
                    self.inverter = not self.inverter
                moved = self.update_position()
                self.update_move()
            elif next_tile in ['#', 'X']:
                # print("#####", ['sober', 'breaker'][self.breaker] , file=sys.stderr, flush=True)
                if self.breaker and next_tile == 'X':
                    moved = self.update_position()
                    self.update_move()
                else:
                    if not blocked:
                        self.dir = ['SOUTH', 'WEST'][self.inverter]
                        self.state.save(self.get_present_state()) 
                        blocked = True
                    else:
                        self.change_direction()
            elif next_tile in ['E', 'S', 'N', 'W']:
                moved = self.update_position()
                modifier = {'E': 'EAST', 'S': 'SOUTH', 'N': 'NORTH', 'W': 'WEST'}
                self.dir = modifier[next_tile]
                # print("--MOD--", self.dir , next_tile, file=sys.stderr, flush=True)
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

