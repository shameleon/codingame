import sys
import math

""" progress 100%
BFS is more suitable for finding the shortest path 
or the closest node to the starting node

issue : need to remove links that were blocked
"""


class Graph:
    def __init__(self, nb_nodes, nb_links, nb_gateways):
        """ Adjacency list """
        self.n = nb_nodes
        self.l = nb_links
        self.e = nb_gateways
        self.nodes = range(self.n)
        self.adj_list = {node: set() for node in self.nodes}
        self.gateways = {node: False for node in self.nodes} 

    def add_edge(self, node1, node2):
        self.adj_list[node1].add(node2)
        self.adj_list[node2].add(node1)

    def add_gateway(self, node):
        self.gateways[node] = True

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print("node", key, ": ", self.adj_list[key], file=sys.stderr, flush=True)
        for key in self.gateways.keys():
            print("gateway",key, ": ", self.gateways[key], file=sys.stderr, flush=True)

    def severing_path(self, start):
        """Finding shortests path for each gateway,
        then overall shortest path, which last link  will be severedd"""
        pathes = []
        for gateway in self.gateways:
            if self.gateways[gateway]:
                path = self.shortest_path(start, gateway)
                pathes.append(path)
                print("path to", gateway, ":", path, file=sys.stderr, flush=True)
        shortest = get_shortest_list(pathes)
        print("target path", shortest, file=sys.stderr, flush=True)
        if len(shortest) >= 2:
            print(shortest[-2], shortest[-1])

    def shortest_path(self, node1, node2):
        """BFS, thus avoiding backtracking, 
        List of the listed pathes"""
        pathes = [[node1]]
        idx = 0
        visited = {node1}
        if node1 == node2:
            return pathes[0]       
        while idx < len(pathes):
            current = pathes[idx]
            last = current[-1]
            children = self.adj_list[last]
            if node2 in children:
                current.append(node2)
                return current
            for next_node in children:
                if not next_node in visited:
                    new_path = current[:]
                    new_path.append(next_node)
                    pathes.append(new_path)
                    visited.add(next_node)
            idx += 1
        return []

@staticmethod
def get_shortest_list(lsts):
    lens = [len(lst) for lst in lsts]
    idx = lens.index(min(lens))
    return lsts[idx]

def main():
    """ 
    n: the total number of nodes in the level, including the gateways
    l: the number of links
    e: the number of exit gateways
    """
    n, l, e = [int(i) for i in input().split()]
    graph = Graph(n, l, e)

    for i in range(l):
        # n1: N1 and N2 defines a link between these nodes
        n1, n2 = [int(j) for j in input().split()]
        graph.add_edge(n1, n2)
    for i in range(e):
        ei = int(input())  # the index of a gateway node
        graph.add_gateway(ei)
    graph.print_adj_list()
    # game loop
    turn = 0
    while True:
        si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
        print("agent at", si, file=sys.stderr, flush=True)
        graph.severing_path(si)
        turn += 1
        

if __name__ == "__main__":
    main()