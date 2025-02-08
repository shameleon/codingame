import sys
from time import time


class Node:
    def __init__(self, node_id):
        self.id = node_id

class DFS:
    def __init__(self, nb_bombs):
        self.nb_bombs = nb_bombs
        self.nb_nodes = 8
        self.nodes = [Node(node_id) for node_id in range(self.nb_nodes )]
        self.best_scores = {7: [0, 2], 8: [4], 9:[5, 6], 10: [4, 5], 11: [7],
                            12: [6], 13: [0, 1, 6, 7], 14: [1], 15:[2], 
                            16:[4, 5], 17:[6], 18:[5], 
                            24: [2, 3], 25: [0, 1, 2, 5]
                            }
        self.solution_found = False
        self.winner_bombs = None
        self.search_best_combination([], set(), nb_bombs)
        if self.winner_bombs:
            print("Solution found :", self.winner_bombs)
        else:
            print("No Solution was found :(")

    def search_best_combination(self, comb: list, nodes_to_be_destroyed: set, nb_bombs):
        if self.solution_found:
            return
        if len(nodes_to_be_destroyed) == self.nb_nodes:
            self.solution_found = True
            self.winner_bombs = comb
            return
        if nb_bombs == 0:
            return
        for key in range(7, 16, 1):
            if key not in comb:
                new_comb = comb + [key] 
                new_nodes = nodes_to_be_destroyed | set(self.best_scores[key])
                self.search_best_combination(new_comb, new_nodes, nb_bombs - 1)

def main():
    time_start = time()
    dfs = DFS(3)
    print(round((time() - time_start) * 1000000) / 1000, "ms", file=sys.stderr, flush=True)

if __name__ == '__main__':
    sys.exit(main())