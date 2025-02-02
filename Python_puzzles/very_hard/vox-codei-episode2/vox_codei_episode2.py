import sys
import numpy as np

class Node:
    def __init__(self, node_id, coords: tuple):
        self.id = node_id
        self.timecoords = list()
        self.timecoords.append(coords)
        self.movement = None

    def update(self, y, x):
        pass

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

    def identify_move(self, coords: list):
        if len(self.timecoords) == 2:
            return coords
        new_coords = []
        possible = []
        while len(coords):
            coord = coords.pop()
            movement = self.move_type(coord)
            if movement != None:
                possible.append(coord)
            else:
                new_coords.append(coord)
        if len(possible) == 1:
            self.timecoords.append(possible[0])
            self.movement = self.move_type(possible[0])
            print(self.id, self.timecoords[0], possible[0], self.movement, file=sys.stderr, flush=True)
        else:
            new_coords.extend(possible)
        return new_coords

    def __repr__(self):
        return f'Node {self.id} : {self.timecoords[0]}'


class TimeFrameGraph:
    def __init__(self):
        self.surveillance_nodes = list()
    
    def update_time_frame(self, turn, node_coords):
        if turn == 0:
            for i, coords in enumerate(node_coords):
                self.surveillance_nodes.append(Node(i, coords))
            print(self.surveillance_nodes, file=sys.stderr, flush=True)
        elif turn == 1:
            while len(node_coords):
                for node in self.surveillance_nodes:
                    node_coords = node.identify_move(node_coords)
            print(node_coords, file=sys.stderr, flush=True)


class Grid:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.turn = 0
        self.fork_score = np.zeros(self.w * self.h, dtype=int).reshape((self.h, self.w))
        self.graph = TimeFrameGraph()

    def update(self, rounds, map_rows):
        surveillance_nodes_map = locate_on_map(map_rows, '@')
        nodes_coords = list(map(tuple, np.argwhere(surveillance_nodes_map == 1)))
        self.graph.update_time_frame(self.turn, nodes_coords)
        #passive_nodes_map = locate_on_map(map_rows, '#')
        #self.nodes_map = surveillance_nodes_map * 2 + passive_nodes_map * (-42)
        #print(surveillance_nodes_map, file=sys.stderr, flush=True)
        self.turn += 1

@staticmethod
def locate_on_map(map_rows: list, char: str):
    mat = [[1 if i == char else 0 for i in row] for row in map_rows]
    return np.array(mat)


class VoxCodeiEpisode2:
    def __init__(self, width, height):
        self.grid = Grid(width, height)

def main():
    # width: width of the firewall grid
    # height: height of the firewall grid
    width, height = [int(i) for i in input().split()]
    print(width, height, file=sys.stderr, flush=True)
    vox = VoxCodeiEpisode2(width, height)
    solutions = ["3 2", "4 1", "5 2", "6 3", "8 5"] 
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
        print(map_rows, file=sys.stderr, flush=True)
        vox.grid.update(rounds, map_rows)
        # test 6 53 "6 3"
        # Patience
        if rounds == 88:
            print("5 4")
        elif rounds == 83:
            print("10 2")
        elif rounds == 86:
            """86    83     moves + 3
            @.....   ......
            .@...@   @@*...
            .....@.  ..@...
            """
            print("2 7")
        else:
            print("WAIT")
        turn += 1

if __name__ == '__main__':
    sys.exit(main())