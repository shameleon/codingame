#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;


struct          Cell
{
    int pos;
    int i;
    int j;
    Cell(int pos, int i, int j):pos(pos), i(i), j(j){
    }
};

// Find the minimum number of moves to reach each cell from the starting point
class   Pathfinder
{
    private:
        vector < vector<int>>           _dir ={{0,1},{1,0},{0,-1},{-1,0}};
        string                          _move = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int                             _h, _w;
        vector <vector <char>>          _maze;
        vector <pair <int, int>>        _path;
        queue <Cell>                  _q;

        int             checkMove(char c);
        void            checkBounds(int &i, int &j);
        void            nextMove(Cell cell);

    public:
        Pathfinder(vector <vector <char>> &maze, vector <pair <int, int>> &start, int h, int w);
        ~Pathfinder(void){};

        void            findShortPath(void);
        int             getMazeH(void){ return this->_h; }
        vector<char>    &getMazeLine(int i){ return this->_maze[i]; }
};

Pathfinder::Pathfinder(vector <vector <char>> &maze, vector <pair <int, int>> &start,
                        int h, int w):_maze(maze), _path(start), _h(h), _w(w)
{
    cerr << "starts at (" << _path.front().first << ", " << _path.front().second << ")" << endl;
}

int         Pathfinder::checkMove(char c){
    size_t      index = _move.find(c);
    if (index != string::npos)
        return index;
    else
        return -1;
}

void        Pathfinder::checkBounds(int &i, int &j)
{
    if (i == -1)
        i = _h - 1;
    else if (i == _h)
        i = 0;
    else if (j == -1)
        j = _w - 1;
    else if (j == _w)
        j = 0;
}

void        Pathfinder::nextMove(Cell cell)
{
    for(int d = 0; d < 4; d++){
        int next_i = cell.i + _dir[d][0];
        int next_j = cell.j + _dir[d][1];
        checkBounds(next_i, next_j);
        if (_maze[next_i][next_j] == '.'){
            Cell      next(cell.pos + 1, next_i, next_j);
            _maze[next_i][next_j] = _move[next.pos];
            _q.push(next);
        }
    }
    while (!_q.empty())
    {
        Cell  next = _q.front();
        _q.pop();
        nextMove(next);
    }
}

void        Pathfinder::findShortPath(void)
{
    Cell    start(0, _path.front().first, _path.front().second);
    _maze[start.i][start.j] = _move[0];
    nextMove(start);
}

ostream			&operator<<(ostream& oss, Pathfinder &rhs)
{
    for (int i = 0; i < rhs.getMazeH(); i++){
        vector<char> line = rhs.getMazeLine(i);
        for (vector<char>::iterator it = line.begin(); it < line.end(); ++it)
            oss << *it; 
        oss << endl;
    }
    return oss;
}

int     main()
{
    vector <vector <char>>    maze;
    vector <pair <int, int>>        start;
    int                             w, h;

    cin >> w >> h; cin.ignore();
    for (int i = 0; i < h; i++) {
        string                      row;
        getline(cin, row);
        cerr << row << endl;
        maze.push_back(vector <char>());
        for (string::iterator it = row.begin(); it < row.end(); ++it){
            maze[i].emplace_back(*it);
            if (*it == 'S')
                start.push_back({i, it - row.begin()});
        }
    }
    Pathfinder      my_maze(maze, start, h, w);

    cerr << endl;
    my_maze.findShortPath();
    cout << my_maze;

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
}
