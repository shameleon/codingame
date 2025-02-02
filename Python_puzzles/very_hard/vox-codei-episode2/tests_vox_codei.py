import sys

#from vox_codei_episode2 import VoxCodeiEpisode2

class Node:
    def __init__(self, node_id, coords: tuple):
        self.id = node_id
        self.timecoords = list()
        self.timecoords.append(coords)
        self.movement = None

    def move_type(self, coord):
        y, x = coord
        yi, xi = self.timecoords[0]
        if abs(y - yi) == 1 and x == xi:
            return ['vertic', x]
        elif abs(x - xi) == 1 and y == yi:
            return ['horizo', y]
        elif y == yi and x == xi:
            return 'static'
        return None
    
    def __repr__(self):
        return f'Node {self.id} : {self.timecoords[0]}'

class TimeFrameGraph:
    def __init__(self):
        self.surveillance_nodes = list()
        self.time_frame = list()

    def add_coords_at_time(self, nodes_coords):
        if len(self.time_frame) == 0:
            for i, coords in enumerate(nodes_coords):
                self.surveillance_nodes.append(Node(i, coords))
        self.time_frame.append(nodes_coords)
    
    def find_nodes_movements(self):
        """ test with one node """
        print('---')
        node = self.surveillance_nodes[5]
        print(node)
        print('---')
        firsts = list()
        for move in self.time_frame[1]:
            res = node.move_type(move)
            if res:
                print(move, res)
                firsts.append(move)
        print('---')
        for first in firsts:
            for move in self.time_frame[2]:
                res2 = self.are_close(first, move)
                if res2:
                    print(res2)
        print('---')


    def are_close(self, coord_i, coord):
        y, x = coord
        yi, xi = coord_i
        if abs(y - yi) == 1 and x == xi:
            return ['vertic', x]
        elif abs(x - xi) == 1 and y == yi:
            return ['horizo', y]
        elif y == yi and x == xi:
            return 'static'
        return None


class VoxCodeiEpisode2:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.graph = TimeFrameGraph()
    
    def update(self, rounds, map_rows):
        self.record_node_movement(map_rows)
        if self.turn == 2:
            self.graph.find_nodes_movements()
        self.turn += 1

    def record_node_movement(self, map_rows):
        nodes = []
        for i, map_row in enumerate(map_rows):
            for j, c in enumerate(map_row):
                if c == '@':
                    nodes.append(tuple([i, j]))
        self.graph.add_coords_at_time(nodes)


class Test08:
    """Indestructible nodes, 4 bombs"""
    def map_dimensions(self):
        return "12 9"
    
    def get_round_map(self, turn):
        if turn == 0:
            return "60 4", ['........@...', '.......@....', '.#.#.#@#.#.#', '.....@......', '#.#.@#..#.#.', '...@........', '..@.........', '.@..........', '@...........']
        elif turn == 1:
            return "59 4", ['.......@....', '........@...', '.#.#.#.#.#.#', '....@.@.....', '#.#..#..#.#.', '..@.........', '...@........', '............', '.@..........']
        elif turn == 2:
            return "58 4", ['......@.....', '.........@..', '.#.#@#.#.#.#', '.......@....', '#.#..#@.#.#.', '.@..........', '....@.......', '.@..........', '..@.........']
        elif turn == 3:
            return "57 4", ['.....@......', '....@.....@.', '.#.#.#.#.#.#', '........@...', '#.#..#..#.#.', '@.....@.....', '.@...@......', '............', '...@........']

class Test05:
    """Indestructible nodes, 4 bombs"""
    def map_dimensions(self):
        return "12 9"
    
    def get_round_map(self, turn):
        if turn == 0:
            return "99 9", ['.#.@........', '..#......@..', '......@..#..', '.....@....#.', '....@...#...', '...@.......#', '..@......#..', '.@......#...', '@......#....']
        elif turn == 1:
            return "98 9", ['.#..@.......', '..#.....@...', '.......@.#..', '......@...#.', '.....@..#...', '....@......#', '...@.....#..', '..@.....#...', '.@.....#....']
        elif turn == 2:
            return "97 9", ['.#...@......', '..#....@....', '........@#..', '.......@..#.', '......@.#...', '.....@.....#', '....@....#..', '...@....#...', '..@....#....']

class Test03:
    """Indestructible nodes, 4 bombs"""
    def map_dimensions(self):
        return "12 9"
    
    def get_round_map(self, turn):
        if turn == 0:
            return "50 7", ['..@....@....', '...........@', '.@..........', '.....@......', '@...........', '............', '............', '.@..........', '............']
        elif turn == 1:
            return "49 7", ['..@........@', '.......@....', '@...........', '............', '.@...@......', '............', '............', '..@.........', '............']
        elif turn == 2:
            return "48 7", ['..@.........', '...........@', '.@.....@....', '............', '..@.........', '.....@......', '............', '...@........', '............']


def main():
    test = Test08()
    width, height = test.map_dimensions().split()
    print(width, height, file=sys.stderr, flush=True)
    vox = VoxCodeiEpisode2(width, height)
    for turn in range(4):
        rounds_bombs, map_rows = test.get_round_map(turn)
        rounds, bombs = rounds_bombs.split()
        print(rounds, bombs, file=sys.stderr, flush=True)
        print(map_rows, file=sys.stderr, flush=True)
        vox.update(rounds, map_rows)
    for line in vox.graph.time_frame:
        print(line)


if __name__ == '__main__':
    sys.exit(main())


