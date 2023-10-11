import sys
import math
import numpy as np

""" progress : 94 % """


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
        print(self.grid, file=sys.stderr, flush=True)
        self.turn = 0
        self.level = 0
        self.forkbombs = []
        self.surveillance_nodes = []
        self.destroyed = []
        for y in range(self.h):
            for x in range(self.w):
                if self.grid[y][x] == '@':
                    self.surveillance_nodes.append([y, x, 1])
                elif self.grid[y][x] == '#':
                    self.surveillance_nodes.append([y, x, -42])
        #print(self.surveillance_nodes, file=sys.stderr, flush=True)
        self._firewall_analysis(1)

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
        print(self.surveillance_nodes, file=sys.stderr, flush=True)
        if np.sum(fork_score) > 0:
            print("score \n", fork_score, file=sys.stderr, flush=True)
            for n in range(1):
                row, col = np.where(fork_score == fork_score.max())
                #print(row[n], col[n], file=sys.stderr, flush=True)
                if wait == 0:
                    if bomb_order == 1 and fork_score.max() >= 5:
                        wait = 3
                    self.forkbombs.append(ForkBomb(row[n], col[n], bomb_order, wait))
                    print("bomb", row[n], col[n], bomb_order, file=sys.stderr, flush=True)
                    self._to_be_destroyed(row[n], col[n])
                else:
                    wait -= 1
                self._countdown()
                self._firewall_analysis(bomb_order + 1, wait)


    def update(self, rounds, bombs):
        print("-------- round ", rounds, "--------", file=sys.stderr, flush=True)
        print("bombs \n", len(self.forkbombs), file=sys.stderr, flush=True)
        self.bombs = bombs
        if self.turn == 0:
            if len(self.forkbombs) > bombs:
                self.reevaluate = True
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
