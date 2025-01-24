import sys
import math

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.parents = []
        self.is_leaf = True
        self.is_root = True
        self.level = 0

    def add_child(self, child):
        self.children.append(child)
        self.is_leaf = False

    def add_parent(self, parent):
        self.parents.append(parent)
        self.is_root = False

    def add_level(self, level):
        self.level = max(self.level, level)
        for child in self.children:
            child.add_level(self.level + 1)

    def __repr__(self):
        children_ids = [child.id for child in self.children]
        parents_ids = [parent.id for parent in self.parents]
        return f'{self.id} : --> {children_ids}  <-- {parents_ids}  \tlevel:{self.level}'


class Graph:
    def __init__(self):
        self.nodes = []
        nb_of_edges = int(input())
        for i in range(nb_of_edges):
            edge = list(map(int, input().split()))
            print(edge, file=sys.stderr, flush=True)
            self.add_vertex(edge)

    def get_node(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def create_if_not_existing(self, node_id):
        node = self.get_node(node_id)
        if node == None:
            node = Node(node_id)
            self.nodes.append(node)
        return node
    
    def add_vertex(self, edge):
        parent = self.create_if_not_existing(edge[0])
        child = self.create_if_not_existing(edge[1])
        parent.add_child(child)
        child.add_parent(parent)

    def find_longest_succession(self):
        roots = [node for node in self.nodes if node.is_root]
        for root in roots:
            root.add_level(1)
        leaves = [node for node in self.nodes if node.is_leaf]
        successions = []
        for leaf in leaves:
            successions.append(leaf.level)
        print(successions, file=sys.stderr, flush=True)
        return max(successions)

    def __repr__(self):
        result = []
        for node in self.nodes:
            result.append(node.__repr__())
        return '\n'.join(result)


def main():
    graph = Graph()
    print(graph.find_longest_succession())
    print(graph, file=sys.stderr, flush=True)


if __name__ == '__main__':
    sys.exit(main())
