/* from Phind
In c++, how to Find the minimum number of moves to reach each cell of a maze from a given starting point
Answer | phind Model

To find the minimum number of moves to reach each cell of a maze from a given starting point in C++, you can use a modified Breadth-First Search (BFS) algorithm. This algorithm is commonly used for solving maze problems, as it can efficiently find the shortest path to a destination node in a graph.

Here's a step-by-step approach to implementing the BFS algorithm for this problem:

    Create a queue and push the starting node into the queue.
    Mark the starting node as visited.
    While the queue is not empty, perform the following steps: a. Dequeue the front node from the queue. b. If the dequeued node is the destination, return the distance (number of moves) from the starting node. c. If the dequeued node is not visited, mark it as visited. d. Enqueue all unvisited adjacent nodes of the dequeued node.
    If the destination node is not found, return a large value to indicate that the destination is not reachable.

Here's a sample C++ implementation:
*/
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int min_moves(int maze[N][N], int start, int end) {
    int moves[N][N];
    int n = sizeof(maze) / sizeof(maze[0]);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            moves[i][j] = -1;
        }
    }

    queue<pair<int, int>> q;
    q.push({0, start});

    moves[start][end] = 0;

    while (!q.empty()) {
        int current = q.front().first;
        int current_node = q.front().second;
        q.pop();

        if (current_node == end) {
            return moves[start][end];
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (maze[current_node][i] == maze[i][current_node] &&
                    maze[current_node][j] == maze[j][current_node]) {
                    int next_node = (i + 1) % n;
                    int next_node_j = (j + 1) % n;
                    q.push({maze[current_node][i], current_node});
                    q.push({maze[current_node][j], current_node});
                    q.push({maze[current_node][next_node], current_node});
                    q.push({maze[current_node][next_node_j], current_node});
                }
            }
        }
    }

    return -1;
}

int main() {
    int maze[N][N];
    // Fill the maze with the starting node at position 0
    maze[0][0] = 1;
    maze[0][1] = 0;
    maze[0][2] = 0;
    maze[1][0] = 0;
    maze[1][1] = 1;
    maze[1][2] = 0;
    maze[2][0] = 0;
    maze[2][1] = 0;
    maze[2][2] = 1;

    int start = 0;
    int end = 2;

    cout << "Minimum moves to reach cell " << end << " from cell " << start << " is: " << min_moves(maze, start, end) << endl;

    return 0;
}

/*
This implementation assumes that the maze is represented as a 2D array, where 0 indicates a free cell, and 1 indicates a wall. The min_moves function takes the maze, the starting node, and the destination node as input and returns the minimum number of moves required to reach the destination from the starting node.

Note that this implementation does not handle negative moves (moving in the opposite direction) or diagonal moves. If you need to handle these cases, you can modify the BFS algorithm to consider these additional moves.

The BFS algorithm can also be adapted to solve other maze-related problems, such as finding the shortest path from a starting point to all other cells or finding the shortest path between two arbitrary points in the mazei.*/
