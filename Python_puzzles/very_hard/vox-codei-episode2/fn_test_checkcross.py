import sys


class TestCross:
    def __init__(self):
        self.w, self.h = (12, 9)
        self.blocks_coords = [(2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (2, 11), (4, 0), (4, 2), (4, 5), (4, 8), (4, 10)]
        #self.nodes_pos = [(0, 6), (1, 1), (0, 6), (3, 3), (6, 4), (5, 11), (6, 6), (5, 1), (8, 8)]
        self.nodes_pos = [(3, 3)]

    def load_prediction_at_turn(self):
        nodes_pos = self.nodes_pos
        self.print_nodes_on_map(nodes_pos)
        score = 0
        max_tile = None
        scores = []
        for i in range(self.h):
            s = ''
            for j in range(self.w):
                tup = tuple([i, j])
                if tup in nodes_pos or tup in self.blocks_coords:
                    s += str(0)
                else:
                    tile_score = self.check_cross(nodes_pos, tup)
                    s += str(tile_score)
                    if tile_score > score:
                        max_tile = tup
                        score = tile_score
            scores.append(s)
        print("pos", max_tile, "score", score)
        print('\n'.join(scores))
        print(self.blocks_coords)
        print(nodes_pos)

    def check_cross(self, nodes_pos, tup):
        score = 0
        targets = []
        for y, x in nodes_pos:
            if y == tup[0] and abs(tup[1] - x) <= 3:
                score += 1
                targets.append(tuple([y, x]))
                for k in range(min(tup[1], x) + 1, max(tup[1], x)):
                    if tuple([y, k]) in self.blocks_coords:
                        score = 0
            elif x == tup[1] and abs(tup[0] - y) <= 3:
                score += 1
                targets.append(tuple([y, x]))
                for k in range(min(tup[0], y) + 1, max(tup[0], y)):
                    if tuple([k, x]) in self.blocks_coords:
                        score = 0               
        if tup == (3, 6):
            print('nodes', nodes_pos)
            print('bomb targets', targets)
        return score
    
    def print_nodes_on_map(self, nodes_coords):
        grid = ['.' * self.w] * self.h
        for y, x in nodes_coords:
            grid[y] = grid[y][:x] +  '@' + grid[y][x + 1:]
        for y, x in self.blocks_coords:
            grid[y] = grid[y][:x] +  '#' + grid[y][x + 1:]
        print('\n'.join(grid))


def main():
    testcross = TestCross()
    testcross.load_prediction_at_turn()

if __name__ == '__main__':
    sys.exit(main())