#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
pair <int, int>     getMaxShore(vector <pair <int, int>> &island_queue)
{
    pair <int, int>     best;
    int                 max_shore = -1;

    for (vector <pair <int, int>>::iterator it = island_queue.begin(); it != island_queue.end(); ++it){
        int             shore=  it->second;
        cerr << it->first << " " << endl;
        if (it->second > max_shore){
            max_shore = it->second;
            best.first = it->first;
            best.second = it->second;
        }
    }
    return best;
}

int     countShore(vector <vector <char>>  &map, char c)
{
    int     count = 0;

    for(vector <vector <char>>::iterator  it1 = map.begin(); it1 != map.end(); ++it1){
		for(vector <char>::iterator it2 = it1->begin();it2 != it1->end();++it2)
			if (*it2 == c)
            {
                *it2 = '~';
                count++;
            }
    }
    return count;
}

void    printMap(vector <vector <char>>  &map)
{
    vector <vector <char>>::iterator      it1;
    vector <char>::iterator               it2;

    for(it1 = map.begin(); it1 != map.end(); ++it1){
		for(it2 = it1->begin();it2 != it1->end();++it2)
			cerr << *it2;
		cerr << endl;
    }
}

void    exploreIsland(vector <vector <char>>  &map, int y, int x)
{
    //queue <pair <int, int>>                 q;
    vector<vector<int>> dir ={{0,1},{1,0},{0,-1},{-1,0}};
    //try all 4 directions from the current cell
    for(int d = 0; d < 4; d++){
        int adj_y= y + dir[d][0];
        int adj_x= x + dir[d][1];
        if (adj_y < 0 || adj_x < 0 || adj_y >= map.size() || adj_x >= map[y].size())
            continue;
        if (map[y][x] == '#' && map[adj_y][adj_x] == '~')
            map[adj_y][adj_x] = '.';
    }
    // mark visited
    if (map[y][x] == '#')
            map[y][x] = 'V';
    for(int d = 0; d < 4; d++){
        int adj_y= y + dir[d][0];
        int adj_x= x + dir[d][1];
        if (adj_y < 0 || adj_x < 0 || adj_y >= map.size() || adj_x >= map[y].size())
            continue;
        if (map[adj_y][adj_x] == '#')
            exploreIsland(map, adj_y, adj_x);
    }
}

void    getNextIsland(vector <vector <char>>  &map, int island_id, vector <pair <int, int>> &island_queue)
{
    int                                     y = 0;
    int                                     x = 0;

    for (y = 0; y < map.size(); ++y ){
        for(x = 0; x < map[y].size(); ++x){
            if (map[y][x] == '#'){
                cerr << "island origin (" << y << ", " << x << ")" << endl;
                exploreIsland(map, y, x);
                int shore = countShore(map, '.');
                island_id++;
                island_queue.push_back({island_id, shore});
            }
        }
    }
}

int     main(void)
{
    int n;
    cin >> n; cin.ignore();
    vector <vector <char>>      map;
    vector <pair <int, int>>    island_queue;

    for (int i = 0; i < n; i++) {
        string row;
        getline(cin, row);
        map.push_back(vector<char>());
        for (string::iterator it = row.begin(); it < row.end(); ++it)
            map[i].emplace_back(*it);
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    
    cerr << endl;
    printMap(map);
    getNextIsland(map, 0, island_queue);

    pair <int, int>     winner_island = getMaxShore(island_queue);
    cerr << endl;
    cout << winner_island.first << " " << winner_island.second << endl;
    return (0);
}

//https://www.geeksforgeeks.org/find-the-number-of-islands-using-dfs/
