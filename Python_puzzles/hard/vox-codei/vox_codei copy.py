import sys
import math
import numpy as np

class ForkBomb:
    def __init__(self, x, y, crosscount):
        self.x = x
        self.y = y
        self.crosscount = crosscount
    

class VoxCodei:
    def __init__(self, width, height, grid):
        self.w = width
        self.h = height
        self.grid = grid
        # print(self.grid, file=sys.stderr, flush=True)
        self.nodes = []
        self.map = np.zeros(width * height, dtype=int).reshape((height, width))
        for x in range(self.w):
            for y in range(self.h):
                if grid[y][x] == '@':
                    self.map[y][x] = 1
        # print(self.map, file=sys.stderr, flush=True)
        self.countdown = np.zeros(width * height, dtype=int).reshape((height, width))

    def _firewall_analysis(self):
        sum_x = np.sum(self.map, axis=0)
        sum_y = np.sum(self.map, axis=1)
        fork_bombs = np.zeros(self.w * self.h, dtype=int).reshape((self.h, self.w))
        for x in range(self.w):
            for y in range(self.h):
                if self.map[y][x] == 0 and self.countdown[y][x] == 0:
                    fork_bombs[y][x]= sum_x[x] + sum_y[y]
        print("sums \n", fork_bombs, file=sys.stderr, flush=True)
        row, col = np.where(fork_bombs == fork_bombs.max())
        print(col[0], row[0], file=sys.stderr, flush=True)
        self.nodes.append(ForkBomb(col[0], row[0], fork_bombs.max()))
        print("+++ \n", self.map[row[0], :], file=sys.stderr, flush=True)
        print("+++ \n", self.map[:, col[0]] * 3, file=sys.stderr, flush=True)

    def _cross_counter(self, x, y):
        """count the occurence of a character c at row y and col x"""
        return 

    def update(self, rounds, bombs):
        print("-------- round ", rounds, "--------", file=sys.stderr, flush=True)
        self.rounds = rounds
        self.bombs = bombs
        self.countdown[self.countdown > 0] -= 1
        self._firewall_analysis()
        if bombs > 0:
            self._next_bomb()
        else:
            print(self.nodes[0].x, self.nodes[0].y)

    def _next_bomb(self):
        bomb = self.nodes[0]
        print(bomb.x, bomb.y)
        self.countdown[bomb.y, :] = self.map[bomb.y, :] * 3
        self.countdown[:, bomb.x] = self.map[:, bomb.x] * 3
        self.map[bomb.y, :] = 0
        self.map[:, bomb.x] = 0
        print("countdown\n", self.countdown, file=sys.stderr, flush=True)
        self.nodes.clear()
        self._firewall_analysis()


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

