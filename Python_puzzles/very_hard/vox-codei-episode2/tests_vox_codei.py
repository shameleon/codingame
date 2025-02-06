import sys

#from vox_codei_episode2 import VoxCodeiEpisode2


class ForkBomb:
    def __init__(self, turn_to_explode:int, coords:tuple, node_ids: list):
        self.coords = coords
        self.turn_to_place = turn_to_explode - 3
        self.nodes_ids = node_ids
        self.placed = False


class Node:
    def __init__(self, node_id, coords: tuple):
        self.id = node_id
        self.timecoords = list()
        self.timecoords.append(coords)
        self.move_type = list()
        self.predicted_pos = dict()

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
            #print(f'node{self.id} blocks = {self.blocks} limits = {self.boundaries}', file=sys.stderr, flush=True)

    def update_node_movement(self, move_type, first_move, second_move):
        self.move_type.extend(move_type)
        self.timecoords.extend([first_move, second_move])

    def predict_pos_at_next_turn(self) -> tuple:
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
            
    def plan_next_move(self, t: int):
        """ next_move based on 2 last moves"""
        move_dir, idx = self.move_type
        if move_dir == 'vertic':
            y1 = self.predicted_pos[t - 2][0]
            y2 = self.predicted_pos[t - 1][0]
            y3 = y2 + (y2 - y1)
            if y3 in self.boundaries:
                y3 = y1
            next_move = tuple([y3, idx])
        elif move_dir == 'horizo':
            x1 = self.predicted_pos[t - 2][1]
            x2 = self.predicted_pos[t - 1][1]
            x3 = x2 + (x2 - x1)
            if x3 in self.boundaries:
                x3 = x1
            next_move = tuple([idx, x3])
        else:
            next_move = self.predicted_pos[0]
        self.predicted_pos[t] = next_move
        

    def predict_all_next_moves(self, turn, rounds: int):
        """anticipate moves"""
        t = 0
        for coord in self.timecoords:
            self.predicted_pos[t] = coord
            t += 1
        while t < rounds:
            self.plan_next_move(t)
            t += 1
        #print(f'node{self.id} next moves = {self.predicted_pos}', file=sys.stderr, flush=True)

    def __repr__(self): 
        return f'Node {self.id} : {self.timecoords[0]} > {self.timecoords[1]} > {self.timecoords[2]} = {self.move_type}'


class EarlyTimeFrameGraph:
    """caracterize node movement from map datapoints """
    def __init__(self):
        self.surveillance_nodes = list()
        self.time_frame = list()

    def add_coords_at_time(self, nodes_coords):
        """create surveillance nodes instances and loads data for the current timepoint """
        if len(self.time_frame) == 0:
            for i, coords in enumerate(nodes_coords):
                self.surveillance_nodes.append(Node(i, coords))
        self.time_frame.append(nodes_coords)
    
    def find_nodes_movements(self, turn: int):
        """find node movement from the first 3 turns"""
        if turn != 2:
            return
        for node in self.surveillance_nodes:
            initial_pos = node.timecoords[0]
            for first_move in self.time_frame[1]:
                if self.are_close(initial_pos, first_move):
                    self.is_second_move_aligned_with(node, initial_pos, first_move)

    def is_second_move_aligned_with(self, node:Node, initial_pos: tuple, first_move:tuple):
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
        """detemine if both input tuples are compatible with node movement pattern"""
        y0, x0 = initial_pos
        y1, x1 = first_move
        along_col = abs(x1 - x0) == 1 and y1 == y0
        along_row = abs(y1 - y0) == 1 and x1 == x0
        static_node = y1 == y0 and x1 == x0
        return along_col or along_row or static_node
    
    def get_nodes_position_at(self, ft, delta_t=0):
        if delta_t == 0:
            return [node.predicted_pos[ft] for node in self.surveillance_nodes]
        nodes_pos = list()
        for k in range(delta_t):
             nodes_pos.extend([node.predicted_pos[ft + k] for node in self.surveillance_nodes])
        return nodes_pos


class VoxCodeiEpisode2:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.graph = EarlyTimeFrameGraph()
        self.chars = {'nodes': '@', 'blocks': '#'}
    
    def update(self, rounds, bombs, map_rows):
        self.record_node_movement(map_rows)
        self.graph.find_nodes_movements(self.turn)
        self.predict_nodes_future_positions(rounds, map_rows) ## rounds
        if self.turn == 3:
            for t in range(7, 55):
                self.load_prediction_at_turn(t)
        self.turn += 1

    def record_node_movement(self, map_rows):
        nodes_coords = self.get_coordinates_from_map(map_rows, 'nodes')
        self.graph.add_coords_at_time(nodes_coords)

    def predict_nodes_future_positions(self, rounds, map_rows):
        """third turn only :
        select blocks that might affect displacment of the surveillance node.
        That info is passed to nodes so that they ca predict their guture moves"""
        if self.turn != 2:
            return
        self.blocks_coords = self.get_coordinates_from_map(map_rows, 'blocks')
        for node in self.graph.surveillance_nodes:
            node.register_blocks(self.blocks_coords)
            node.set_boundaries(self.w, self.h)
            node.predict_all_next_moves(self.turn, rounds)
    
    def load_prediction_at_turn(self, future_turn):
        ft = future_turn
        if ft < 2:
            return
        nodes_pos = self.graph.get_nodes_position_at(ft)
        nodes_future_pos = self.graph.get_nodes_position_at(ft, 3)
        # self.print_nodes_on_map(nodes_pos)
        score = 0
        max_tile = None
        scores = []
        for i in range(self.h):
            s = ''
            for j in range(self.w):
                tup = tuple([i, j])
                if tup in nodes_future_pos or tup in self.blocks_coords:
                    s += '0'
                else:
                    tile_score = self.check_cross(nodes_pos, tup)
                    s += str(tile_score)
                    if tile_score > score:
                        max_tile = tup
                        score = tile_score
            scores.append(s)
        self.create_new_forkbomb(ft, max_tile)
        # print("time=",ft,"pos", max_tile, "score", score)
        #print('\n'.join(scores))
    
    def check_cross(self, nodes_pos, tup):
        score = 0
        for y, x in nodes_pos:
            if y == tup[0] and abs(tup[1] - x) <= 3:
                score += 1
                for k in range(min(tup[1], x) + 1, max(tup[1], x)):
                    if tuple([y, k]) in self.blocks_coords:
                        score = 0
            elif x == tup[1] and abs(tup[0] - y) <= 3:
                score += 1
                for k in range(min(tup[0], y) + 1, max(tup[0], y)):
                    if tuple([k, x]) in self.blocks_coords:
                        score = 0
        return score
    
    def create_new_forkbomb(self, ft, max_tile):
        node_ids = list()
        for node in self.graph.surveillance_nodes:
            if self.check_cross([node.predicted_pos[ft]], max_tile) == 1:
                node_ids.append(node.id)
        print(ft, max_tile, node_ids)#ForkBomb(ft, max_tile, node_ids)

    def get_coordinates_from_map(self, map_rows: list, key: str):
        """for a given key char, extract corresponding coordinates on the maps"""
        coords_list = []
        for i, map_row in enumerate(map_rows):
            coords_list.extend([tuple([i, j]) for j, c in enumerate(map_row) if c == self.chars[key]])
        return coords_list

    def print_nodes_on_map(self, nodes_coords: list):
        char = self.chars['nodes']
        grid = ['.' * self.w] * self.h
        for y, x in nodes_coords:
            grid[y] = grid[y][:x] +  self.chars['nodes'] + grid[y][x + 1:]
        for y, x in self.blocks_coords:
            grid[y] = grid[y][:x] +  self.chars['blocks'] + grid[y][x + 1:]
        print('\n'.join(grid))

class TestVoxCodei2:
    def __init__(self):
        self.map_dimensions = "12 9"

    def get_map_dimensions(self):
        return self.map_dimensions
    
    def get_round_map(self, turn):
        rounds_and_bombs = ' '.join([str(self.rounds_and_bombs[0] - turn), 
                                     str(self.rounds_and_bombs[1])
                                     ])
        return rounds_and_bombs, self.map_rows[turn]

class Test09(TestVoxCodei2):
    """Patience, 3 bombs"""
    def __init__(self):
        super().__init__()
        self.a_solution = {88: "5 4", 83: "10 2", 86: "2 7"}
        self.rounds_and_bombs = [90, 3]
        self.map_rows = {0: ['@...........', '.....@....@.', '@...........', '.....@......', '..@.@.@.@...', '.....@......', '............', '.@...@......', '.........@.@'],
                         1: ['.@..........', '.....@....@.', '............', '@....@......', '..@.@.@.@...', '.....@......', '............', '.@...@.....@', '........@...'],
                         2: ['..@.........', '.....@....@.', '............', '.....@......', '@.@.@.@.@...', '.....@......', '...........@', '.@...@......', '.......@....'],
                         3: ['...@........', '.....@....@.', '............', '.....@......', '..@.@.@.@...', '@....@.....@', '............', '.@...@......', '......@.....']
                         }


class Test08(TestVoxCodei2):
    """Indestructible nodes, 4 bombs"""
    def __init__(self):
        super().__init__()
        self.a_solution = {}
        self.rounds_and_bombs = [60, 4]
        self.map_rows = {0: ['........@...', '.......@....', '.#.#.#@#.#.#', '.....@......', '#.#.@#..#.#.', '...@........', '..@.........', '.@..........', '@...........'],
                         1: ['.......@....', '........@...', '.#.#.#.#.#.#', '....@.@.....', '#.#..#..#.#.', '..@.........', '...@........', '............', '.@..........'],
                         2: ['......@.....', '.........@..', '.#.#@#.#.#.#', '.......@....', '#.#..#@.#.#.', '.@..........', '....@.......', '.@..........', '..@.........'],
                         3: ['.....@......', '....@.....@.', '.#.#.#.#.#.#', '........@...', '#.#..#..#.#.', '@.....@.....', '.@...@......', '............', '...@........'],
                         }


class Test06(TestVoxCodei2):
    """4 moving nodes, 1 bombs"""
    def __init__(self):
        super().__init__()
        self.a_solution = {}
        self.rounds_and_bombs = [55, 1]
        self.map_rows = {0: ['#..........#', '............', '....#.@#....', '..@.........', '...#....#...', '...........@', '....#..#....', '............', '#....@.....#'],
                         1: ['#..........#', '............', '....#..#....', '...@..@.....', '...#....#...', '..........@.', '....#..#....', '.....@......', '#..........#'],
                         2: ['#..........#', '............', '....#..#....', '....@.......', '...#..@.#...', '.........@..', '....#@.#....', '............', '#..........#'],
                         3: ['#..........#', '............', '....#..#....', '.....@......', '...#....#...', '.....@@.@...', '....#..#....', '............', '#..........#']
                         }


class Test05(TestVoxCodei2):
    """Indestructible nodes, 4 bombs"""
    def __init__(self):
        super().__init__()
        self.a_solution = {}
        self.rounds_and_bombs = [99, 9]
        self.map_rows = {0: ['.#.@........', '..#......@..', '......@..#..', '.....@....#.', '....@...#...', '...@.......#', '..@......#..', '.@......#...', '@......#....'],
                         1: ['.#..@.......', '..#.....@...', '.......@.#..', '......@...#.', '.....@..#...', '....@......#', '...@.....#..', '..@.....#...', '.@.....#....'],
                         2: ['.#...@......', '..#....@....', '........@#..', '.......@..#.', '......@.#...', '.....@.....#', '....@....#..', '...@....#...', '..@....#....'],
                         3: ['.#....@.....', '..#...@.....', '.......@.#..', '........@.#.', '.......@#...', '......@....#', '.....@...#..', '....@...#...', '...@...#....'],
                         }


def main():
    test = Test06()
    width, height = map(int, test.get_map_dimensions().split())
    #print(width, height, file=sys.stderr, flush=True)
    vox = VoxCodeiEpisode2(width, height)
    for turn in range(4):
        rounds_bombs, map_rows = test.get_round_map(turn)
        rounds, bombs = map(int, rounds_bombs.split())
        #print(rounds, bombs, file=sys.stderr, flush=True)
        #print(map_rows, file=sys.stderr, flush=True)
        vox.update(rounds, bombs, map_rows)
    # for line in vox.graph.time_frame:
    #     print(line, file=sys.stderr, flush=True)


if __name__ == '__main__':
    sys.exit(main())


