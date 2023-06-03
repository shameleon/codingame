#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;


struct Cell{
    bool visited = false;
    int step = -1;
    int x,y;
    bool isWall;
    bool isStart;

    Cell(int x , int y, bool isWall, bool isStart):x(x),y(y), isWall(isWall), isStart(isStart){
        if(isStart){
            step = 0;
            visited = true;
        }
    }
};


int main()
{
    int w;
    int h;
    cin >> w >> h; cin.ignore();
    vector<string> map;
    vector<vector<Cell>> cells;
    deque<Cell*> queue;
    for (int i = 0; i < h; i++) {
        string row;
        getline(cin, row);
        vector<Cell> c;

        for(int y = 0; y < row.size();y++){
            bool isWall = row.at(y) =='#';
            bool isStart = row.at(y) == 'S';
            c.emplace_back(Cell(i,y,isWall,isStart));
        }

        cells.emplace_back(c);
        cerr << row <<endl;
    }

    for( int x = 0 ; x < h;x++){
        for(int y = 0 ; y < w;y++){
            if (cells[x][y].isStart){
                queue.emplace_back(&cells[x][y]);
            }
        }
    }

    vector<pair<int,int>> directions {{-1,0},{1,0},{0,-1},{0,1}};
    while(!queue.empty()){
        auto current = queue.front();
        queue.pop_front();
        cerr << "For current: " << current->x << "," << current->y << endl;
        for(auto direction : directions){
            int x = (current->x + direction.first +h)%h;
            int y = (current->y + direction.second + w) %w;
            
            if ( x < 0 || y < 0 || x >= h || y >= w) continue;
            if(cells[x][y].visited || cells[x][y].isWall) continue;

            queue.emplace_back(&cells[x][y]);
            cells[x][y].step = current->step + 1;
            cells[x][y].visited = true;
        }

    }




    for (int i = 0; i < h; i++) {

        for(auto c: cells[i]){
            if(c.isWall){
                cout << "#";
            }else if(c.step >=0){
                if (c.step > 9){
                    cout << char(c.step + 55);
                }else{
                    cout << c.step;
                }
            }else{
                cout << ".";
            }
        }
        cout <<endl;
    }
}
