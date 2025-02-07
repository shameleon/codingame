import sys
from time import time
from tests_vox_codei import Test01, Test02, Test03, Test05, Test06, Test07, Test08, Test09


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
        if self.move_type[1] < 0:
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

    def predict_pos_at_next_turn(self) -> tuple:
        """anticipate next turn move"""
        move_dir, idx = self.move_type
        if move_dir in ['horizo', 'vertic']:
            i = {'vertic': 0, 'horizo': 1}[self.move_type[0]]
            p1, p2 = [p[i] for p in self.timecoords[-2:]]
            p3 = p2 + (p2 - p1)
            if p3 in self.boundaries:
                p3 = p1
            return [tuple([p3, idx]), tuple([idx, p3])][i]
        return self.timecoords[0]
            
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
            print("graph.nodes_coords", nodes_coords, file=sys.stderr, flush=True)
            for i, coords in enumerate(nodes_coords):
                self.surveillance_nodes.append(Node(i, coords))
        self.time_frame.append(nodes_coords)
    
    def find_nodes_movements(self, turn: int):
        """find node movement from the first 3 turns"""
        if turn != 2:
            return
        for node in self.surveillance_nodes:
            self.search_moves(node)
            print(node)

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


class VoxCodeiNodeMovement:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.graph = EarlyTimeFrameGraph()
        self.chars = {'nodes': '@', 'blocks': '#'}

    def update(self, rounds, bombs, map_rows):
        self.record_node_movement(map_rows)
        self.graph.find_nodes_movements(self.turn)
        self.predict_nodes_future_positions(rounds, map_rows)
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

    def get_coordinates_from_map(self, map_rows: list, key: str):
        """for a given key char, extract corresponding coordinates on the maps"""
        coords_list = []
        for i, map_row in enumerate(map_rows):
            coords_list.extend([tuple([i, j]) for j, c in enumerate(map_row) if c == self.chars[key]])
        return coords_list
    

def main():
    tests = [Test01, Test02, Test03, Test05, Test06, Test07, Test08, Test09]
    for test in tests:
        current = test()
        print("-" * 50, type(current).__name__, file=sys.stderr, flush=True)
        width, height = map(int, current.get_map_dimensions().split())
        time_start = time()
        vox = VoxCodeiNodeMovement(width, height)
        for turn in range(4):
            rounds_bombs, map_rows = current.get_round_map(turn)
            rounds, bombs = map(int, rounds_bombs.split())
            vox.update(rounds, bombs, map_rows)
        print(round((time() - time_start) * 1000000) / 1000, "ms", file=sys.stderr, flush=True)


if __name__ == '__main__':
    sys.exit(main())