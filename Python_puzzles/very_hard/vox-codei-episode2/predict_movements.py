import sys

from tests_vox_codei import TestVoxCodei2, Test05, Test06, Test08, Test09


""" """



def main():
    test = Test06()
    width, height = map(int, test.get_map_dimensions().split())
    #print(width, height, file=sys.stderr, flush=True)
    #vox = VoxCodeiEpisode2(width, height)
    for turn in range(4):
        rounds_bombs, map_rows = test.get_round_map(turn)
        rounds, bombs = map(int, rounds_bombs.split())
        #print(rounds, bombs, file=sys.stderr, flush=True)
        #print(map_rows, file=sys.stderr, flush=True)
       # vox.update(rounds, bombs, map_rows)
    # for line in vox.graph.time_frame:
    #     print(line, file=sys.stderr, flush=True)


if __name__ == '__main__':
    sys.exit(main())