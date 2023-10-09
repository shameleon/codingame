import sys
from vox_codei import ForkBomb, VoxCodei

""" width: width of the firewall grid
    height: height of the firewall grid
    Game loop:
    rounds: number of rounds left before the end of the game
    bombs: number of bombs left
"""


def test_vox_codei(w, h, input):
    vox_codei = VoxCodei(w, h, input)
    rounds, bombs = [15, 10]
    while rounds > 0:
        vox_codei.update(rounds, bombs)
        rounds -= 1

def test6():
    w = 8
    h = 6
    input = ['.@.....@',
             '........',
             '........',
             '........',
             '........',
             '.@.....@']
    res = test_vox_codei(w, h, input)

def test3():
    w = 12
    h = 9
    input =['@...@.......',
            '.......@...@',
            '............',
            '...@.....@..',
            '............',
            '.@..........',
            '......@.....',
            '.........@..',
            '............']
    res = test_vox_codei(w, h, input)

def test1():
    """linear, no overlap"""
    w = 5
    h = 3
    input = [".....", ".@...", "....."]
    res = test_vox_codei(w, h, input)

def main():
    #test1()
    test3()
    #test6()


if __name__ == "__main__":
    main()