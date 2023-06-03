#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Find the minimum number of moves to reach each cell from the starting point
class   Pathfinder
{
    private:
        string              _moves = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int                 _h, _w;
        vector<string>      _maze;

        Pathfinder(void) {}
        Pathfinder(Pathfinder   &other){}
        Pathfinder  &operator=(Pathfinder &rhs){}
        char   to_char(int index){ return this->_moves[index]; }
        int     increment(char c){
            size_t      index = this->_moves.find(c);
            if (index != string::npos - 1)
                return index + 1;
            return -1;
        }

        void   check_bounds(int &y, int &x)
        {
            if (x == this->_w)
                x = 0;
            else if (x < 0)
                x = this->_w - 1;
            else if (y == this->_h)
                y = 1;
            else if (y < 0)
                y = this->_h - 1;
        }
        int   fill_maze(int y, int x, int move)
        {
            check_bounds(y, x);
            if (this->_maze[y][x] == '#')
                return 0;
            if (this->_maze[y][x] == '.' || to_char(move) < this->_maze[y][x] )
            {
                this->_maze[y][x] = to_char(move);
                int next = increment(this->_maze[y][x]);
                cerr << "(" << y << ", " << x << ") " << move << ">>" << next << " "<< this->_maze[y][x] << endl;
                fill_maze(y,     x + 1, next);
                fill_maze(y,     x - 1, next);
                fill_maze(y + 1, x,     next);
                fill_maze(y - 1, x,     next);
            }
            return 0;
        }

    public:
        Pathfinder(vector<string> &maze, int &h, int &w):_maze(maze), _h(h), _w(w){}
        ~Pathfinder(void) {}

        void    pathWithStart(int &y, int &x)
        {
            if (x != -1 && y != -1)
                this->fill_maze(y, x, 0);
        }
        int       getMazeH(void){ return this->_h; }
        string    &getMazeLine(int i){ return this->_maze[i]; }
};

ostream			&operator<<(ostream& oss, Pathfinder &rhs)
{
    for (int line = 0; line < rhs.getMazeH(); line++)
        oss << rhs.getMazeLine(line) << endl;
	return oss;
}

int main()
{
    int     w;
    int     h;
    cin >> w >> h; cin.ignore();
    vector <string>      maze;
    int     x = -1;
    int     y = -1;

    for (int i = 0; i < h; i++) {
        string      row;
        getline(cin, row);
        cerr << row << endl;
        maze.push_back(row);
        size_t      found = row.find('S');
        if (found != string::npos)
        {
            x = found;
            y = i;
            maze[y][x] = '.';
        }
    }
    Pathfinder      moves_in_maze(maze, h, w);
    moves_in_maze.pathWithStart(y, x);
    cout << moves_in_maze;
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
}

/* https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/ */
