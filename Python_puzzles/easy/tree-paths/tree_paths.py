import sys
import math


""" progress 0%"""

class Node:
    def __init__(self, p, l=None, r=None):
        self.index = p
        self.left = l
        self.right = r
        self.parent = None
        self.visited = False

    def children_nodes(self, node_l, node_r):
        self.left = node_l
        self.right = node_r

    def parent_node(self, parent):
        self.parent = parent


class BinaryTree:
    def __init__(self, n, v, m):
        self.n = n
        self.v = v
        self.m = m
        self.nodes = []
        for i in range(n):
            self.nodes.append(Node(i + 1))

    def _find_node(self, idx):
        for node in self.nodes:
            if node.index == idx:
                return node
        return None

    def set_children(self, p, l, r):
        parent = self._find_node(p)
        left = self._find_node(l)
        right = self._find_node(r)
        if parent:
            parent.children_nodes(left, right)
            if left:
                left.parent_node(parent)
            if right:
                right.parent_node(parent)
    
    def find_path(self, path=[], idx=None):
        if not idx:
            idx = 1
        node = self._find_node(idx)
        node.visited= True
        if not node:
            return
        while(node.index != self.v):
            self.find_path(path, node.left.index)
            self.find_path(path, node.right.index)

    def print_tree(self):
        for node in self.nodes:
            print(node.index, ":", node.left, node.right, file=sys.stderr, flush=True)


def main():
    """ 
    n: number of nodes in the tree
    v: the index of the target node.
    m: the number of nodes with two children.
    
    P is the node index
    L is the left children of P
    R is the right children of P
    """

    n = int(input())
    v = int(input())
    m = int(input())
    bintree = BinaryTree(n, v, m)
    print(n, v, m, file=sys.stderr, flush=True)
    for i in range(m):
        p, l, r = [int(j) for j in input().split()]
        print(p, ":", l, r, file=sys.stderr, flush=True)
        bintree.set_children(p, l, r)
    bintree.print_tree()
    bintree.find_path()



if __name__ == "__main__":
    main()

# To debug: print("Debug messages...", file=sys.stderr, flush=True)