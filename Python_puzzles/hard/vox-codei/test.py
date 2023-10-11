import sys
from vox_codei import ForkBomb, VoxCodei

""" width: width of the firewall grid
    height: height of the firewall grid
    Game loop:
    rounds: number of rounds left before the end of the game
    bombs: number of bombs left
"""


def test_vox_codei(w, h, input, params):
    vox_codei = VoxCodei(w, h, input)
    rounds, bombs = params
    while rounds > 0:
        vox_codei.update(rounds, bombs)
        rounds -= 1

def test11():
    w = 15
    h = 12
    input = ['...............', 
             '...#...@...#...',
             '....#.....#....',
             '.....#.@.#.....',
             '......#.#......',
             '...@.@...@.@...',
             '......#.#......',
             '.....#.@.#.....',
             '....#.....#....',
             '...#...@...#...',
             '...............',
             '...............']
    res = test_vox_codei(w, h, input, [15, 4])


def test9():
    w = 8
    h = 6
    input = ['........',
             '......@.',
             '@@@.@@@@',
             '......@.',
             '........',
             '........']
    res = test_vox_codei(w, h, input, [10, 2])


def test7():
    w = 12
    h = 9
    input = ['............',
             '..##....##..',
             '.#@@#..#@@#.',
             '............',
             '.#@@#..#@@#.',
             '..##....##..', 
             '............',
             '............',
             '............']
    res = test_vox_codei(w, h, input, [15, 4])

def test6():
    w = 8
    h = 6
    input = ['.@.....@',
             '........',
             '........',
             '........',
             '........',
             '.@.....@']
    res = test_vox_codei(w, h, input, [5, 2])

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
    res = test_vox_codei(w, h, [15, 4])

def test1():
    """linear, no overlap"""
    w = 5
    h = 3
    input = [".....", ".@...", "....."]
    res = test_vox_codei(w, h, [15, 1])

def main():
    # test1()
    # test3()
    # test6()
    # test7()
    # test9()
    test11()


if __name__ == "__main__":
    main()