import sys
import numpy as np

"""
100% success
https://www.codingame.com/ide/puzzle/network-cabling
"""

def main():
    n = int(input())
    xs = []
    ys = []
    xs_min = np.inf
    xs_max = -np.inf
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        if x < xs_min:
            xs_min = x
        if x > xs_max:
            xs_max = x
        xs.append(x)
        ys.append(y)
    horizontal_cable = abs(xs_min - xs_max)
    y_median = round(np.median(ys))
    vertical_cables = np.sum(np.abs(np.add(np.array(ys), - y_median)))
    print(horizontal_cable + vertical_cables)


if __name__ == '__main__':
    sys.exit(main())


"""
### older version - subject not understood
class CablePath:
    def __init__(self, start: tuple, end: tuple):
        self.start = start
        self.end = end
        self.length = abs(end[0] - start[0])
        self.length += abs(end[1] - start[1])
        print("cable", self.start, self.end, self.length, file=sys.stderr, flush=True)

class NetworkCabling:
    def __init__(self, buildings: list):
        self.not_connected = buildings
        self.center = self.get_center(buildings)
        print("buildings", buildings, file=sys.stderr, flush=True)
        print("center :", self.center, file=sys.stderr, flush=True)
        self.in_network = []
        self.in_network.append(self.center)
        self.cables = []
        self.add_cables()
        #self.find_closest_to_node(self.center)
        print(self.not_connected, file=sys.stderr, flush=True)
        print(self.in_network, file=sys.stderr, flush=True)
        print(len(self.cables), file=sys.stderr, flush=True)

    def add_cables(self):
        while len(self.not_connected):
            center = self.get_center(self.in_network)
            i = self.get_closest(self.not_connected, center)
            if i is not None:
                j = self.get_closest(self.in_network, self.not_connected[i])
                if j is not None:
                    network_node = self.in_network[j]
                    node_to_connect = self.not_connected.pop(i)
                    new_cable = CablePath(node_to_connect, network_node)
                    self.cables.append(new_cable)
                    self.in_network.append(node_to_connect)                    

            

    def find_closest_to_node(self, node: tuple):
        idx = self.get_closest(self.not_connected, node)
        if idx is not None:
            closest = self.not_connected.pop(idx)
            print("closest", closest, file=sys.stderr, flush=True)
            new_cable = CablePath(closest, node)
            self.cables.append(new_cable)
            self.in_network.append(closest)
            
    def get_closest(self, edges: list, node: tuple) -> tuple:
        idx_min = None
        dist_min = math.inf
        for i, edge in enumerate(edges):
            distance = self.get_distance(edge, node)
            if distance < dist_min:
                idx_min = i
                dist_min = distance
        print(idx_min, file=sys.stderr, flush=True)
        return idx_min

    @staticmethod
    def get_center(nodes: list) -> tuple:
        avg_x = sum(list(zip(*nodes))[0]) / len(nodes)
        avg_y = sum(list(zip(*nodes))[1]) / len(nodes)
        return tuple([round(avg_x), round(avg_y)])

    @staticmethod
    def get_distance(a: tuple, b: tuple) -> int:
        return abs(b[0] - a[0]) + abs(b[1] - a[1]) 

    def __repr__(self):
        network_length = 0
        for cable in self.cables:
            network_length += cable.length
        return f'{network_length}'

def main():
    n = int(input())
    print(n, file=sys.stderr, flush=True)
    buildings = []
    for i in range(n):
        building = tuple([int(j) for j in input().split()])
        buildings.append(building)
    network = NetworkCabling(buildings)
    print(network)


if __name__ == '__main__':
    sys.exit(main())
"""
