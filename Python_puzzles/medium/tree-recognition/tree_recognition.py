import sys


class Node:
    def __init__(self, data, id_number):
        self.left = None
        self.right = None
        self.data = data
        if data:
            self.id = id_number
        #print(self.id, ':', self.data, file=sys.stderr, flush=True)
    
    def insert(self, data):
        n = self.id
        if data < self.data:
            if self.left is None:
                self.left = Node(data, 2 * n + 1)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, 2 * n + 2)
            else:
                self.right.insert(data)
        else:
            self.data = data


class Tree:
    def __init__(self, input_line):
        node_values = input_line.split()
        print(*node_values, file=sys.stderr, flush=True)
        head = node_values.pop(0)
        self.root = Node(int(head), 0)
        for data in node_values:
            self.root.insert(int(data))
        self.node_ids = []
        self.get_node_id(self.root)
    
    def get_node_id(self, node):
        if node :
            if node.id:
                self.node_ids.append(node.id)
            self.get_node_id(node.left)
            self.get_node_id(node.right)
    
    def __repr__(self):
        return str(sorted(self.node_ids))


class TreeRecognition:
    def __init__(self):
        self.trees = []
        self.unique_shapes = []

    def add_tree(self, input_line):
        tree = Tree(input_line)
        self.trees.append(tree)

    def print_trees(self):
        print("_" * 100, file=sys.stderr, flush=True)
        for tree in self.trees:
            print(tree, file=sys.stderr, flush=True)
        print("_" * 100, file=sys.stderr, flush=True)
    
    def count_unique_shapes(self):
        for tree in self.trees:
            shape = tree.__repr__()
            if shape not in self.unique_shapes:
                self.unique_shapes.append(shape)
        return len(self.unique_shapes)


def main():
    n, k = [int(i) for i in input().split()]
    recognition = TreeRecognition()
    for i in range(n):
        recognition.add_tree(input())
    recognition.print_trees()
    print(recognition.count_unique_shapes())


if __name__ == '__main__':
    sys.exit(main())
