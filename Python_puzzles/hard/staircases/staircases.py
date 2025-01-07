import sys
import math


"""
Jan 6th 2025 Community Event
Puzzles Classic puzzle - Hard 
Staircases By sampriti

The program:
Given N bricks, your program needs to find the number of different staircases that can be built using all of these bricks.

A staircase consists of steps of different sizes in a strictly increasing order. Two steps can not have the same height. Every staircase has a minimum of 2 steps and each step has at least 1 brick.

Example:

For N = 5, there are two different valid staircases that can be built
1 then 4 bricks
2 then 3 bricks
"""


class Staircases:
    def __init__(self, nb_bricks):
        """
            Finds number of possible staircases made with all the bricks
            
            nb_bricks : nb of bricks to build staircases
            memoization : mem[nb of bricks left][current step height]
        """
        self.mem = [ [-1]*501 for i in range(501) ]
        self.nb_stairs = self.build_step(nb_bricks - 1, 1) - 1

    def build_step(self, bricks: int, height: int) -> int:
        if bricks < 0:
            return 0
        if bricks == 0:
            return 1
        if self.mem[bricks][height] == -1:
            self.mem[bricks][height] = self.build_step(bricks - 1, height + 1) \
                                     + self.build_step(bricks - (height + 1), height + 1)
        return self.mem[bricks][height]

    def __repr__(self):
        return f'{self.nb_stairs}'


if __name__ == "__main__":
    print(Staircases(int(input())))