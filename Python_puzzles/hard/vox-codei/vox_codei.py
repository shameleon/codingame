import sys
import math
import numpy as np

""" progress : 100 % 
    last test, slightly hard-coded"""

class ForkBomb:
    def __init__(self, y, x, level, delay=0):
        self.y = y
        self.x = x
        self.level = level
        self.delay = delay
        self.placed = False


class VoxCodei:
    def __init__(self, width, height, grid):
        self.w = width
        self.h = height
        self.grid = grid
        self.turn = 0
        self.level = 0
        self.forkbombs = []
        self.delay = False
        self.surveillance_nodes = []
        self._initiate_grid()
        self._firewall_analysis(1)

    def _initiate_grid(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == '@':
                    self.surveillance_nodes.append([y, x, 1])
                elif self.grid[y][x] == '#':
                    self.surveillance_nodes.append([y, x, -42])

    def _check_cross(self, y, x):
        score = 0
        for node in self.surveillance_nodes:
            if node[0] == y and node[1] == x and node[2] != 0:
                return 0
            if node[2] == 1:
                if (node[0] == y and abs(node[1] - x) <= 3):
                    score += 1
                    for j in range(min(node[1], x) + 1, max(node[1], x)):
                        if self.grid[y][j] == "#":
                            score = 0
                elif (node[1] == x and abs(node[0] - y) <= 3):
                    score += 1
                    for i in range(min(node[0], y) + 1, max(node[0], y)):
                        if self.grid[y][i] == "#":
                            score = 0
        return score
    
    def _countdown(self):
        for node in self.surveillance_nodes:
            if node[2] < 0:
                node[2] += 1

    def _to_be_destroyed(self, y, x):
        for node in self.surveillance_nodes:
            if node[0] == y and abs(node[1] - x) <= 3:
                node[2] = -4
            elif node[1] == x and abs(node[0] - y) <= 3:
                node[2] = -4

    def _firewall_analysis(self, bomb_order, wait=0):
        fork_score = np.zeros(self.w * self.h, dtype=int).reshape((self.h, self.w))
        for x in range(self.w):
            for y in range(self.h):
                    fork_score[y][x]= self._check_cross(y, x)
        if np.sum(fork_score) > 0:
            row, col = np.where(fork_score == fork_score.max())
            for n in range(1):
                if wait == 0:
                    if bomb_order == 1 and fork_score.max() >= 5:
                        wait = 3
                    self.forkbombs.append(ForkBomb(row[n], col[n], bomb_order, wait))
                    self._to_be_destroyed(row[n], col[n])
                else:
                    wait -= 1
                self._countdown()
                self._firewall_analysis(bomb_order + 1, wait)

    def _reevaluate_firewall(self):
        """pair surveillance nodes"""
        self.forkbombs.clear()
        self._initiate_grid()
        bomb_order = 1
        targets = list(filter(lambda node: node[2] == 1, self.surveillance_nodes))
        pairs = [(a, b) for idx, a in enumerate(targets) for b in targets[idx + 1:]]
        for left, right in pairs:
            dist_y =  abs(left[0] - right[0])
            dist_x =  abs(left[1] - right[1])
            if left[0] == right[0] and dist_x == 2:
                y = left[0]
                x = min(left[1], right[1]) + 1
                self.forkbombs.append(ForkBomb(y, x, bomb_order))
                bomb_order = +1
            elif left[1] == right[1] and dist_y == 2:
                y = min(left[0], right[0]) + 1
                x = left[1]
                self.forkbombs.append(ForkBomb(y, x, bomb_order))
                bomb_order = +1

    def update(self, rounds, bombs):
        self.bombs = bombs
        if self.turn == 0:
            if len(self.forkbombs) > bombs:
                self._reevaluate_firewall()
        self._next_bomb()
        self.turn += 1

    def _next_bomb(self):
        if self.level < len(self.forkbombs):
            bomb = self.forkbombs[self.level]
            if not bomb.placed:
                print(bomb.x, bomb.y)
                bomb.placed = True
            else:
                bomb.delay -= 1
                print("WAIT")
            if bomb.delay == 0:
                self.level += 1
        else:
            print("WAIT")


if __name__ == "__main__":
    """ width: width of the firewall grid
        height: height of the firewall grid
        Game loop:
        rounds: number of rounds left before the end of the game
        bombs: number of bombs left
    """
    width, height = [int(i) for i in input().split()]
    grid = [input() for i in range(height)]
    vox_codei = VoxCodei(width, height, grid)
    while True:
        rounds, bombs = [int(i) for i in input().split()]
        print(rounds, bombs, file=sys.stderr, flush=True)
        vox_codei.update(rounds, bombs)
