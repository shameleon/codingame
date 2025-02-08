import sys
from time import time

"""
enhancements : 
- backtracking to avoid dead-ends
- a set for seen_solutions to avoir redundant solutions
- sorted best_score to prioritize higher impact bombs first

result : test05 from 317.197 ms to  puis 0.099 ms
"""

class Node:
    def __init__(self, node_id):
        self.id = node_id

class DFS:
    def __init__(self, nb_nodes, nb_bombs, nb_rounds, best_scores):
        self.nb_bombs = nb_bombs
        self.nb_nodes = nb_nodes
        self.nb_rounds =  nb_rounds
        self.nodes = [Node(node_id) for node_id in range(self.nb_nodes )]
        self.sorted_best_scores = sorted(best_scores.items(), key=lambda x: -len(x[1]))
        self.solution_found = False
        self.winner_bombs = None
        self.seen_solutions = set()
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
        state = frozenset(nodes_to_be_destroyed)
        if state in self.seen_solutions:
            return
        self.seen_solutions.add(state)
        for key, nodes in self.sorted_best_scores:
            if key not in comb:
                new_comb = comb + [key] 
                new_nodes = nodes_to_be_destroyed | set(nodes)
                self.search_best_combination(new_comb, new_nodes, nb_bombs - 1)
                if self.solution_found:
                    return


def test05():
    best_scores = {6: [2, 3, 4], 7: [2, 3, 4], 8: [2, 3, 4], 9: [2, 3, 4], 10: [2, 3, 4, 6], 11: [8, 5, 6], 12: [2, 3, 4], 13: [2, 3, 4], 14: [1, 2, 4], 15: [1, 2, 4], 16: [3, 6, 7], 17: [8, 4, 5, 6], 18: [0, 1, 2], 19: [1, 2, 5], 20: [8, 4, 7], 21: [8, 4, 7], 22: [8, 4, 7], 23: [8, 2, 4], 24: [8, 4, 6], 25: [3, 4, 6], 26: [2, 3, 6], 27: [8, 4, 5], 28: [0, 2, 5], 29: [0, 2, 5], 30: [1, 2, 4], 31: [0, 3, 5], 32: [0, 3, 5], 33: [0, 3], 34: [0, 1, 3], 35: [0, 1, 2], 36: [0, 1], 37: [8, 2, 5], 38: [2, 4, 5], 39: [0, 1, 3], 40: [0, 1, 3], 41: [3, 4, 5], 42: [2, 3, 6], 43: [0, 1], 44: [0, 1], 45: [0, 2], 46: [0, 2], 47: [4, 6, 7], 48: [1, 2, 5], 49: [0, 1], 50: [0, 1, 3], 51: [1, 2, 3, 5], 52: [0, 1, 2, 5], 53: [1, 2, 4], 54: [0, 1, 3], 55: [0, 1, 3], 56: [0, 1, 3], 57: [0, 1, 3], 58: [2, 5, 6], 59: [3, 5, 7], 60: [2, 3, 5], 61: [8, 4, 6], 62: [3, 4, 6], 63: [0, 2], 64: [0, 1, 2], 65: [0, 1], 66: [0, 1, 2], 67: [0, 1, 2], 68: [0, 1, 2, 3], 69: [0, 1, 3], 70: [1, 3, 4, 5], 71: [0, 1, 3], 72: [0, 1, 3], 73: [0, 1, 3], 74: [2, 4, 6], 75: [0, 1, 3], 76: [0, 3], 77: [8, 2, 5], 78: [5, 6, 7], 79: [3, 4, 5], 80: [8, 4, 6], 81: [1, 4, 5], 82: [2, 4, 6], 83: [1, 2, 4], 84: [0, 1], 85: [0, 1, 2], 86: [0, 1, 3], 87: [8, 4, 5, 6]}
    return best_scores

def test03():
    best_scores = {6: [2, 5, 6], 7: [1, 4, 5], 8: [2, 5, 6], 9: [3, 5, 6], 10: [2, 3, 5], 11: [2, 5, 6], 12: [1, 3, 5], 13: [1, 3, 4, 5], 14: [4, 5, 6], 15: [3, 4, 5], 16: [1, 3, 5], 17: [0, 3], 18: [0, 3, 5], 19: [0, 3], 20: [3, 5, 6], 21: [0, 3], 22: [0, 3], 23: [3, 4, 5], 24: [4, 5, 6], 25: [0, 3, 4], 26: [0, 3, 4], 27: [1, 3, 5], 28: [1, 3, 4], 29: [1, 3, 4], 30: [0, 1], 31: [2, 3, 5], 32: [1, 3, 5], 33: [1, 3], 34: [1, 5, 6], 35: [2, 3, 5], 36: [4, 5, 6], 37: [3, 5], 38: [3, 4, 5], 39: [4, 5, 6], 40: [0, 3, 5], 41: [0, 3, 4], 42: [3, 5, 6], 43: [0, 3], 44: [0, 4, 5], 45: [0, 3, 4], 46: [4, 5, 6], 47: [3, 4, 5]}
    return best_scores

def main():
    time_start = time()
    dfs = DFS(7, 9, 47, test03())
    print(round((time() - time_start) * 1000000) / 1000, "ms", file=sys.stderr, flush=True)
    time_start = time()
    dfs = DFS(8, 7, 87, test05())
    print(round((time() - time_start) * 1000000) / 1000, "ms", file=sys.stderr, flush=True)

if __name__ == '__main__':
    sys.exit(main())