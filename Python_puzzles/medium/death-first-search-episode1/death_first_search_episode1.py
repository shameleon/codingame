import sys
import math


class Graph:
    def __init__(self, nb_nodes, nb_links, nb_gateways):
        """ Adjacency list """
        self.n = nb_nodes
        self.l = nb_links
        self.e = nb_gateways
        self.nodes = range(self.n)
        self.adj_list = {node: set() for node in self.nodes}
        self.gateways = {node: False for node in self.nodes} 

    def add_edge(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))
        self.adj_list[node2].add((node2, weight))

    def add_gateway(self, node):
        self.adj_list[node1].add((node2, weight))
        self.adj_list[node2].add((node2, weight))

    def print_adj_list(self):
        for key in self.adj_list.keys():
            print("node", key, ": ", self.adj_list[key])

    def dfs(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None   


def main():
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in input().split()]
    graph = Graph(n, l, e)

    for i in range(l):
        # n1: N1 and N2 defines a link between these nodes
        n1, n2 = [int(j) for j in input().split()]
        graph.add_edge(n1, n2)

    for i in range(e):
        ei = int(input())  # the index of a gateway node

    # game loop
    while True:
        si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # Example: 0 1 are the indices of the nodes you wish to sever the link between
        print("1 2")

if __name__ == "__main__":
    main()

