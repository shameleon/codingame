#include <iostream>
#include <string>
#include <list>
#include <tuple>

using namespace std;

int main()
{
    int w, h, i(0);
    cin >> w >> h; cin.ignore();
    string map;
    for (i = 0; i < h; i++) {
        string row;
        getline(cin, row);
        map += row;
    }

    int pos(map.find('S')), depth(0);
    list<pair<int, int>> BFS = { make_pair(pos, depth) };
    map[pos] = '0';
    while (BFS.size() != 0) {
        tie(pos, depth) = BFS.front(); BFS.pop_front();
        if(map[pos] == '.') map[pos] = char((depth < 10) ? '0' + depth : 'A' + depth - 10);
        int neighbors[4] = {pos-1, pos-w, pos+1, pos+w};

        if(neighbors[0] % w == w-1) neighbors[0] += w;
        if(neighbors[2] % w == 0) neighbors[2] -= w;
        if(neighbors[1] < 0) neighbors[1] = w*h + neighbors[1]%w;
        if(neighbors[3] >= w*h) neighbors[3] = neighbors[3]%w;

        for(i = 0; i < 4; i++)
            if(map[neighbors[i]] == '.')
                BFS.push_back(make_pair(neighbors[i], depth+1));
    }

    for (i = 0, pos = 0; i < h; i++, pos+=w) cout.write(&map[pos], w), cout << endl;
}
