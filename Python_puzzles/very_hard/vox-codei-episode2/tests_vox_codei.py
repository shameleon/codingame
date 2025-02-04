import sys

#from vox_codei_episode2 import VoxCodeiEpisode2

class Node:
    def __init__(self, node_id, coords: tuple):
        self.id = node_id
        self.timecoords = list()
        self.timecoords.append(coords)
        self.move_type = list()

    def register_blocks(self, blocks_coords: list):
        """pick blocks"""
        if len(self.move_type) != 2:
            return 
        move_dir, idx = self.move_type
        if move_dir in ['horizo', 'vertic']:
            i = {'horizo': 0, 'vertic': 1}[move_dir]
            self.blocks = [p[1 - i] for p in blocks_coords if p[i] == idx]

    def set_boundaries(self, width, height):
        if self.move_type[0] in ['vertic', 'horizo']:
            i = {'vertic': 0, 'horizo': 1}[self.move_type[0]]
            start = -1
            end = [height, width][i]
            pos = self.timecoords[0][i]
            for block_pos in self.blocks:
                if block_pos < pos:
                    start = max(start, block_pos)
                else:
                    end = min(block_pos, end)
            self.boundaries = [start, end]
            print(f'node{self.id} blocks = {self.blocks} limits = {self.boundaries}', file=sys.stderr, flush=True)

    def update_node_movement(self, move_type, first_move, second_move):
        self.move_type.extend(move_type)
        self.timecoords.extend([first_move, second_move])

    def predict_pos_at_next_turn(self, turn: int) -> tuple:
        """anticipate next turn move"""
        move_dir, idx = self.move_type
        if move_dir == 'vertic':
            y1, y2 = [p[0] for p in self.timecoords[-2:]]
            y3 = y2 + (y2 - y1)
            if y3 in self.boundaries:
                y3 = y1
            return tuple([y3, idx])
        elif move_dir == 'horizo':
            x1, x2 = [p[1] for p in self.timecoords[-2:]]
            x3 = x2 + (x2 - x1)
            if x3 in self.boundaries:
                x3 = x1
            return tuple([idx, x3])
        return self.timecoords[0]
            

    def predict_moves(self, turn):
        """anticipate moves"""

        if self.move_type == 'horizo':
            pass
        pass

    def __repr__(self): 
        return f'Node {self.id} : {self.timecoords[0]} > {self.timecoords[1]} > {self.timecoords[2]} = {self.move_type}'


class TimeFrameGraph:
    def __init__(self):
        self.surveillance_nodes = list()
        self.time_frame = list()

    def add_coords_at_time(self, nodes_coords):
        if len(self.time_frame) == 0:
            for i, coords in enumerate(nodes_coords):
                self.surveillance_nodes.append(Node(i, coords))
        self.time_frame.append(nodes_coords)
    
    def find_nodes_movements(self, turn: int):
        """find node movement in the first 3 turns """
        if turn != 2:
            return
        for node in self.surveillance_nodes:
            initial_pos = node.timecoords[0]
            for first_move in self.time_frame[1]:
                if self.are_close(initial_pos, first_move):
                    for second_move in self.time_frame[2]:
                        move_type = self.are_aligned(initial_pos, first_move, second_move)
                        if move_type != None:
                            node.update_node_movement(move_type, first_move, second_move)
                            print(node, file=sys.stderr, flush=True)

    def are_aligned(self, initial_pos, first_move, second_move):
        """pick coordinates compatible with node linear movement """
        y0, x0 = initial_pos
        y1, x1 = first_move
        y2, x2 = second_move
        if abs(y1 - y0) == 1 and x1 == x0:
            if abs(y2 - y1) == 1 and x2 == x1:
                return ['vertic', x0]
        elif abs(x1 - x0) == 1 and y1 == y0:
            if abs(x2 - x1) == 1 and y2 == y1:
                return ['horizo', y0]
        elif y1 == y0 and x1 == x0:
            if y2 == y1 and x2 == x1:
                return 'static'
        return None

    def are_close(self, initial_pos, first_move):
        """pick first tuple of coordinates compatible initial position """
        y0, x0 = initial_pos
        y1, x1 = first_move
        along_col = abs(x1 - x0) == 1 and y1 == y0
        along_row = abs(y1 - y0) == 1 and x1 == x0
        static_node = y1 == y0 and x1 == x0
        return along_col or along_row or static_node


class VoxCodeiEpisode2:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.graph = TimeFrameGraph()
        self.chars = {'nodes': '@', 'blocks': '#'}
    
    def update(self, rounds, map_rows):
        self.record_node_movement(map_rows)
        self.graph.find_nodes_movements(self.turn)
        self.set_nodes_boundaries(map_rows)
        self.turn += 1

    def record_node_movement(self, map_rows):
        nodes_coords = self.get_coordinates_from_map(map_rows, 'nodes')
        self.graph.add_coords_at_time(nodes_coords)

    def set_nodes_boundaries(self, map_rows):
        """select blocks that might affect displacment of the surveillance node"""
        if self.turn != 2:
            return
        blocks_coords = self.get_coordinates_from_map(map_rows, 'blocks')
        for node in self.graph.surveillance_nodes:
            node.register_blocks(blocks_coords)
            node.set_boundaries(self.w, self.h)
        tmp = []
        for node in self.graph.surveillance_nodes:
            tmp.append(node.predict_pos_at_next_turn(self.turn))
        print(tmp, file=sys.stderr, flush=True)

    def get_coordinates_from_map(self, map_rows: list, key: str):
        coords_list = []
        for i, map_row in enumerate(map_rows):
            for j, c in enumerate(map_row):
                if c == self.chars[key]:
                    coords_list.append(tuple([i, j]))
        return coords_list


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
    width, height = map(int, test.map_dimensions().split())
    print(width, height, file=sys.stderr, flush=True)
    vox = VoxCodeiEpisode2(width, height)
    for turn in range(4):
        rounds_bombs, map_rows = test.get_round_map(turn)
        rounds, bombs = rounds_bombs.split()
        print(rounds, bombs, file=sys.stderr, flush=True)
        print(map_rows, file=sys.stderr, flush=True)
        vox.update(rounds, map_rows)
    for line in vox.graph.time_frame:
        print(line, file=sys.stderr, flush=True)


if __name__ == '__main__':
    sys.exit(main())


