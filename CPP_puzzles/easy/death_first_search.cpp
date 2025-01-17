#include <iostream>
#include <string>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

 // https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
class Graph
{
    public:
    map<int, bool>          visited;
    map<int, list<int> >    adj;
    vector <int>            gateway;
 
    // function to add an edge to graph
    void addEdge(int v, int w);
    void addGateway(int v);
    // DFS traversal of the vertices
    // reachable from v
    void DFS(int v);
};


void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w); // Add w to v’s list.
}

void Graph::addGateway(int e)
{
    gateway.push_back(e); // Add w to v’s list.
}

void Graph::DFS(int v)
{
    // Mark the current node as visited and
    // print it
    visited[v] = true;
    cerr << "agent :" << v << endl;
 
    // Recur for all the vertices adjacent
    // to this vertex
    list<int>::iterator it;
    for (it = adj[v].begin(); it != adj[v].end(); ++it)
        if (!visited[*it])
        {
            DFS(*it);
            cerr << *it << endl;
        }
}
 
int main()
{
    int n; // the total number of nodes in the level, including the gateways
    int l; // the number of links
    int e; // the number of exit gateways
    cin >> n >> l >> e; cin.ignore();
    Graph   g;
    for (int i = 0; i < l; i++) {
        int n1; // N1 and N2 defines a link between these nodes
        int n2;
        cin >> n1 >> n2; cin.ignore();
        g.addEdge(n1, n2);
    }
    vector <int> gateways;
    for (int i = 0; i < e; i++) {
        int ei; // the index of a gateway node
        cin >> ei; cin.ignore();
        g.addGateway(ei);
    }

    // game loop
    while (1) {
        int si; // The index of the node on which the Bobnet agent is positioned this turn
        cin >> si; cin.ignore();
        g.DFS(si);
        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        // Example: 0 1 are the indices of the nodes you wish to sever the link between
        cout << "2 3" << endl;
    }
}