#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;


void    printMap(vector <vector <char> >  &map)
{
    vector <vector <char> >::iterator      it1;
    vector <char>::iterator               it2;

    for(it1 = map.begin(); it1 != map.end(); ++it1){
		for(it2 = it1->begin();it2 != it1->end();++it2)
			cerr << *it2;
		cerr << endl;
    }
}

void    exploreIsland(vector <vector <char> >  &map, vector< vector <bool> >  &visited, int y, int x, int &count)
{
    // mark visited
    if (map[y][x] == 'O') {
        visited[y][x] = true;
        count++;
    }
    //queue <pair <int, int>>                 q;
    int  dir_y[4] = {0, 1, 0, -1};
    int  dir_x[4] = {1, 0, -1, 0};
    //try all 4 directions from the current cell
    for(int d = 0; d < 4; d++)
    {
        int adj_y= y + dir_y[d];
        int adj_x= x + dir_x[d];
        if (adj_y < 0 || adj_x < 0
            || adj_y >= static_cast<int>(map.size()) || adj_x >=  static_cast<int>(map[y].size()))
            continue;
        if (map[y][x] == 'O' && map[adj_y][adj_x] == 'O')
        {
            cerr << adj_x << ", " << adj_y << "    ";
            //map[adj_y][adj_x] = '1';
        }
    }
    for(int d = 0; d < 4; d++)
    {
        int adj_y= y + dir_y[d];
        int adj_x= x + dir_x[d];
        if (adj_y < 0 || adj_x < 0
            || adj_y >= static_cast<int>(map.size()) || adj_x >=  static_cast<int>(map[y].size()))
            continue;
        if (map[adj_y][adj_x] == 'O' && !visited[adj_y][adj_x])
            exploreIsland(map, visited, adj_y, adj_x, count);
    }
}

int lake_area(vector< vector <char> >  &map, int h, int l, int x, int y)
{
    int count = 0;
    if (map[y][x] != '#')
    {
        vector< vector <bool> >  visited(h, vector <bool> (l,false)) ;
        exploreIsland(map, visited, y, x, count);
        cerr << endl;
    }
    return count;
}

int main()
{
    string  row[5];
    int l = 5;
    int h = 5;
    row[0] = "#####";
    row[1] = "#OO##";
    row[2] = "##OO#";
    row[3] = "#OOO#";
    row[4] = "#####";
    vector< vector <char> >  map(h, vector <char> (l, 0)) ;
    for (int i = 0; i < h; i++) {
        string row;

        map.push_back(vector <char>());
        for (int j = 0; j < l; ++j)
        {
            if (row[j] == '#' || row[j] == 'O')
                map[i][j] = row[j];
        }
    }

    //printMap(map);
    
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int x = 2; 
        int y = 2;
        cin >> x >> y; cin.ignore();
        cerr << " x=" << x << "   y=" << y << "    " << map[y][x] << endl;
        cout << lake_area(map, h, l, x, y) << endl;
    }
    printMap(map);
}