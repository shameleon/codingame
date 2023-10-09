import sys
import math
import numpy as np

""" progress 100% """

class PlotOfLand:
    def __init__(self, w, h):
        self.spots = {'.': 0, 'X': 1, 'Y': 11}
        self.land = np.zeros(w * h, dtype=int).reshape((h, w))
        self.w = w
        self.h = h
        self.year = 0
        self.limit = 33

    def initial_seeds_and_trees(self, arr):
        for i in range (self.h):
            print(arr[i], file=sys.stderr, flush=True)
            for j in range (self.w):
                if arr[i][j] == 'Y':
                    self.land[i][j] = 11
                elif arr[i][j] == 'X':
                    self.land[i][j] = 1
        self.add_one_seed(arr)
        # print(self.land, file=sys.stderr, flush=True)
        self.update_each_year()
    
    def add_one_seed(self, arr):
        """ Heuristic to find best spot to plant
        the unique seed. Anticipating trees and seeds growth"""
        land = np.zeros(w * h, dtype=int).reshape((h, w))
        for i in range (self.h):
            for j in range (self.w):
                if arr[i][j] == 'Y':
                    land = 1 * ((land + self.fill_around(i, j, 3)) > 0)
        # print(land, file=sys.stderr, flush=True)
        # print("before", np.sum(land), file=sys.stderr, flush=True)
        best_for_max = []
        max_trees = 0
        for i in range (self.h):
            for j in range (self.w):
                # if land[i][j] == 0:
                trees = np.sum((land + self.fill_around(i, j, 2)) > 0)
                if trees > max_trees:
                    best_for_max.append([i, j, trees])
                    max_trees = trees
        print("seed at:", best_for_max[-1], file=sys.stderr, flush=True)
        seed_i, seed_j, trees = best_for_max[-1]
        # print (self.fill_around(seed_i, seed_j, 2), file=sys.stderr, flush=True)
        self.land[seed_i][seed_j] = 1
        print(self.land, file=sys.stderr, flush=True)

    def fill_around(self, i, j, radius):
        """provides an empty land that is 1-filled 
        around a position i, j for a given radius. 
        parameter : i, j position
            radius=3 for a tree and radius=2 for a seed
        return: np.array shaped (h, w) filled with ones around position"""
        r = radius
        around = np.zeros(w * h, dtype=int).reshape((h, w))
        for k in range (i - r, i + r + 1):
            for m in range (j - r, j + r + 1):
                if 0 <= k < self.h and 0 <= m < self.w:
                    if abs(k - i) + abs(m - j) <= r:
                        around[k][m] = 1
        return around

    def _seed_around(self, seeder_i, seeder_j):
        for tree in range(len(seeder_i)):
            i = seeder_i[tree]
            j = seeder_j[tree]
            if i > 0:
                if self.land[i - 1][j] == 0:
                    self.land[i - 1][j] = 1
            if i + 1 < self.h:
                if self.land[i + 1][j] == 0:
                    self.land[i + 1][j] = 1
            if j > 0:
                if self.land[i][j - 1] == 0:
                    self.land[i][j - 1] = 1
            if j + 1 < self.w:
                if self.land[i][j + 1] == 0:
                    self.land[i][j + 1] = 1

    def update_each_year(self):
        if self.year <= self.limit:
            self.year += 1
            self.land += 1 * (self.land > 0)
            seeder_i, seeder_j = np.where(self.land == 12)
            self._seed_around(seeder_i, seeder_j)
            self.update_each_year()
        else:
            print(self.land, file=sys.stderr, flush=True)
            print(np.sum(self.land >= 11))


if __name__ == "__main__":
    w = int(input())
    h = int(input())
    print(w, h, file=sys.stderr, flush=True)
    my_land = PlotOfLand(w, h)
    arr = [input() for i in range (h)]
    # print(*arr, file=sys.stderr, flush=True)
    my_land.initial_seeds_and_trees(arr)

