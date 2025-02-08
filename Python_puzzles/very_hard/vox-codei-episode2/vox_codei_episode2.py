import sys

""" Codinggame Vox Codei episode 5

Tests :
    Success: 01 02 03 04 06 07
    Failed but succes if start + 10 rounds : 08
    Failed - no more bombs :  05
    Failed - Timeout, no solution:  09
    Failed -  Timeout :  10

Validators : 70% success
    05 09 10 failed

Todo:
    Pruning + decision tree
"""


class ForkBomb:
    def __init__(self, turn_to_explode:int, coords:tuple, node_ids: set):
        self.coords = coords
        self.turn_to_place = turn_to_explode - 2  #### weird why not 4
        self.nodes_ids = node_ids
        self.placed = False

    def __repr__(self):
        return ' '.join(map(str, self.coords[::-1]))


class DepthFirstSearch:
    """search for first solution through instances of forkbombs"""
    def __init__(self, best_scores: set, nb_nodes:int , nb_bombs:int):
        self.nb_bombs = nb_bombs
        self.nb_nodes = nb_nodes
        self.best_scores = best_scores
        self.winner_comb = list()
        self.solution_found = False
        self.search_best_combination([], set(), nb_bombs)

    def search_best_combination(self, comb: list, nodes_to_be_destroyed: set, nb_bombs):
        if self.solution_found:
            return
        if len(nodes_to_be_destroyed) == self.nb_nodes:
            self.solution_found = True
            self.winner_comb = comb
            print("best comb", comb, file=sys.stderr, flush=True)
            return
        if nb_bombs == 0:
            return
        for bomb in self.best_scores:
            if bomb.turn_to_place not in comb:
                new_comb = comb + [bomb.turn_to_place] 
                new_nodes = nodes_to_be_destroyed | set(bomb.nodes_ids)
                self.search_best_combination(new_comb, new_nodes, nb_bombs - 1)

    def get_best_bombs(self):
        if self.winner_comb:
            return [bomb for bomb in self.best_scores if bomb.turn_to_place in self.winner_comb]
        return []

class Node:
    """surveillance node @ """
    def __init__(self, node_id, coords: tuple):
        self.id = node_id
        self.timecoords = list()
        self.timecoords.append(coords)
        self.move_type = list()
        self.predicted_pos = dict()

    def register_blocks(self, blocks_coords: list):
        """pick blocks # that might hinder move along line"""
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
        if self.move_type == []:
            self.move_type.extend(move_type)
            self.timecoords.extend([first_move, second_move])
            
    def plan_next_move(self, t: int):
        """next_move based on 2 last moves"""
        move_dir, idx = self.move_type
        if move_dir in ['horizo', 'vertic']:
            i = {'vertic': 0, 'horizo': 1}[self.move_type[0]]
            p1 = self.predicted_pos[t - 2][i]
            p2 = self.predicted_pos[t - 1][i]
            p3 = p2 + (p2 - p1)
            if p3 in self.boundaries:
                p3 = p1
            self.predicted_pos[t] = [tuple([p3, idx]), tuple([idx, p3])][i]
        else:
            self.predicted_pos[t] = self.predicted_pos[0]

    def predict_all_next_moves(self, rounds: int):
        """anticipate moves at turn == 2
        predicted_pos dict last key should be initial total rounds - 1
        """
        t = 0
        for coord in self.timecoords:
            self.predicted_pos[t] = coord
            t += 1
        stop = t + rounds - 1
        while t < stop:
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
            self.search_moves(node)
            # print(node, file=sys.stderr, flush=True)

    def search_moves(self, node: Node):
        p0 = node.timecoords[0]
        first_moves = self.time_frame[1]
        second_moves = self.time_frame[2]
        p1s = [p1 for p1 in first_moves if self.are_close(p0, p1)]
        for p1 in p1s: 
            p2s = [p2 for p2 in second_moves if self.are_aligned(p0, p1, p2)]
            if len(p2s) == 1:
                p2 = p2s[0]
                move_type = self.are_aligned(p0, p1, p2)
                node.update_node_movement(move_type, p1, p2)
                return
        return

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
                return ['static', -1]
        return None

    def are_close(self, initial_pos, first_move):
        """detemine if both input tuples are compatible with node movement pattern"""
        y0, x0 = initial_pos
        y1, x1 = first_move
        along_col = abs(x1 - x0) == 1 and y1 == y0
        along_row = abs(y1 - y0) == 1 and x1 == x0
        static_node = y1 == y0 and x1 == x0
        return along_col or along_row or static_node
    
    def get_nodes_position_at(self, ft, when_placed=False):
        """provides nodes position at a given turn ft (future time)
        Since bomb explosion is evaluated at turn ft,
        command with print would occurs at t-4, and bomb placed at t-3 cannot be placed on a node"""
        if when_placed:
            return ([node.predicted_pos[ft - 3] for node in self.surveillance_nodes])
        return [node.predicted_pos[ft] for node in self.surveillance_nodes]


class VoxCodeiEpisode2:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.graph = EarlyTimeFrameGraph()
        self.chars = {'nodes': '@', 'blocks': '#'}
        self.best_scores = []
        self.forkbombs = []
    
    def update(self, rounds, bombs, map_rows):
        turn_to_predict = 3
        delay_to_explode = 4
        self.record_node_movement(map_rows)
        self.graph.find_nodes_movements(self.turn)
        self.predict_nodes_future_positions(rounds, map_rows) ## rounds
        if self.turn == turn_to_predict:
            start = 1 + turn_to_predict + delay_to_explode
            stop = turn_to_predict + rounds
            for t in range(start,stop):
                self.load_prediction_at_turn(t)
            #print([f'{x.turn_to_place}{x.coords} {x.nodes_ids}' for x in self.best_scores], file=sys.stderr, flush=True)
            print(', '.join([f'{x.turn_to_place}: {list(x.nodes_ids)}' for x in self.best_scores]), file=sys.stderr, flush=True)
            nb_nodes = len(self.graph.surveillance_nodes)
            self.dfs = DepthFirstSearch(self.best_scores, nb_nodes, bombs)
            self.forkbombs = self.dfs.get_best_bombs()
            print([f'*{x.turn_to_place + 4}:{x.nodes_ids}' for x in self.forkbombs], file=sys.stderr, flush=True)
        self.can_place_a_bomb_at_turn()
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
            node.predict_all_next_moves(rounds)
    
    def load_prediction_at_turn(self, future_turn):
        ft = future_turn
        if ft < 2:
            return
        nodes_pos = self.graph.get_nodes_position_at(ft, False)
        nodes_when_placed_pos = self.graph.get_nodes_position_at(ft, True)
        # self.print_nodes_on_map(nodes_pos)
        score = 0
        max_tile = None
        for i in range(self.h):
            for j in range(self.w):
                tup = tuple([i, j])
                if tup in nodes_when_placed_pos or tup in self.blocks_coords:
                    pass
                else:
                    tile_score = self.check_cross(nodes_pos, tup)
                    if tile_score > score:
                        max_tile = tup
                        score = tile_score
        self.create_new_forkbomb(ft, max_tile)
    
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
    
    def create_new_forkbomb(self, turn_to_explode, max_tile):
        """Bomb instances are just possibilitid that would be explored by DFS"""
        node_ids = set()
        for node in self.graph.surveillance_nodes:
            coord = [node.predicted_pos[turn_to_explode]]
            if self.check_cross(coord, max_tile) == 1:
                node_ids.add(node.id)
        self.best_scores.append(ForkBomb(turn_to_explode, max_tile, node_ids))

    def can_place_a_bomb_at_turn(self):
        for bomb in self.forkbombs:
            if bomb.turn_to_place == self.turn:
                print(f'{bomb.turn_to_place}->*{bomb.nodes_ids}', file=sys.stderr, flush=True)
                return bomb.__repr__()
        return None

    def get_coordinates_from_map(self, map_rows: list, key: str):
        """for a given key char, extract corresponding coordinates on the maps"""
        coords_list = []
        for i, map_row in enumerate(map_rows):
            coords_list.extend([tuple([i, j]) for j, c in enumerate(map_row) if c == self.chars[key]])
        return coords_list

    def print_nodes_on_map(self, nodes_coords: list):
        grid = ['.' * self.w] * self.h
        for y, x in nodes_coords:
            grid[y] = grid[y][:x] +  self.chars['nodes'] + grid[y][x + 1:]
        for y, x in self.blocks_coords:
            grid[y] = grid[y][:x] +  self.chars['blocks'] + grid[y][x + 1:]
        print('\n'.join(grid), file=sys.stderr, flush=True)


def main():
    # width: width of the firewall grid
    # height: height of the firewall grid
    width, height = [int(i) for i in input().split()]
    print(width, height, file=sys.stderr, flush=True)
    vox = VoxCodeiEpisode2(width, height)
    # game loop
    turn = 0
    while True:
        # rounds: number of rounds left before the end of the game
        # bombs: number of bombs left
        rounds, bombs = [int(i) for i in input().split()]
        print(rounds, bombs, file=sys.stderr, flush=True)
        map_rows = []
        for i in range(height):
            map_row = input()  # one line of the firewall grid
            map_rows.append(map_row)
        place_a_bomb = vox.update(rounds, bombs, map_rows)
        if place_a_bomb:
            print(place_a_bomb)
        else:
            print("WAIT")
        turn += 1

if __name__ == '__main__':
    sys.exit(main())