import sys


class Node:
    def __init__(self, node_id):
        self.id = node_id

class DFS:
    def __init__(self, nb_bombs):
        self.nb_bombs = nb_bombs
        self.nb_nodes = 8
        self.nodes = [Node(node_id) for node_id in range(self.nb_nodes )]
        self.best_scores = {7: [0, 2], 8: [4], 9:[5, 6], 10: [4, 5], 
                            11: [1, 6, 7], 12: [6], 13: [0, 1, 6, 7],
                            14: [2, 3], 15: [0, 1, 2, 5]
                            }
        self.solution_found = False
        self.bombs = None
        self.search_best_combination(set(), set(), nb_bombs)
        
    def search_best_combination(self, comb: set, nodes_to_be_destroyed: set, nb_bombs):
        if self.solution_found:
            return
        if len(nodes_to_be_destroyed) == self.nb_nodes:
            print("Solution found :", comb, nodes_to_be_destroyed)
            self.solution_found = True
            self.bombs = comb
            return
        if nb_bombs == 0:
            return
        for key in range(7, 16, 1):
            if key not in comb:
                new_comb = set(comb)
                new_nodes = set(nodes_to_be_destroyed)
                new_comb.add(key)
                new_nodes.update(self.best_scores[key])
                self.search_best_combination(new_comb, new_nodes, nb_bombs - 1)

def main():
    dfs = DFS(3)

if __name__ == '__main__':
    sys.exit(main())