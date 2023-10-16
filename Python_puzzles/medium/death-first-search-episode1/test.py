import sys
from death_first_search_episode1 import Graph

""" 
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
"""


def test_death_first_search(nle, links, gateways, agent):
    graph = Graph(nle[0], nle[1], nle[2])
    for i in range(links):
        n1, n2 = links[i]
        graph.add_edge(n1, n2)
    for i in range(gateways):
        graph.add_gateway(int(gateways[i]))
    for turn in range(agent):
        print("agent", agent[turn], file=sys.stderr, flush=True)
        graph.find_path(agent[turn])
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        turn += 1


def test2():
    """linear, no overlap"""
    nle = {'n': 4, 'l': 4, 'e':1}
    links = [[0, 1], [0, 2], [1, 3], [1, 2]]
    gateways = [3]
    agent = [0, 1, 3]
    res = test_death_first_search(nle, links, gateways, agent)


def test1():
    """linear, no overlap"""
    nle = {'n': 3, 'l': 2, 'e':1}
    links = [[0, 1], [1, 2]]
    gateways = [2]
    agent = [1, 2]
    res = test_death_first_search(nle, links, gateways, agent)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()