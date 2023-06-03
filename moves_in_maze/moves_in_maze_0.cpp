/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   moves_in_maze.cpp                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/25 14:56:31 by jmouaike          #+#    #+#             */
/*   Updated: 2023/05/25 15:12:17 by jmouaike         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

char    to_char(int    move)
{
    if (move < 10)
        return move + '0';
    else
        return move - 10 + 'A';
}

int   from_char(char    c)
{
    if (isdigit(c))
        return c - '0';
    else
        return c - 'A' + 10;
}

// time out and need to replace string in vector
int   fill_maze(vector<string> &maze, int y, int x, int move)
{
    if (maze[y][x] != '#')
    {
        int next;
        if (maze[y][x] == '.' || maze[y][x] == 'S')
            maze[y][x] = to_char(move);
        next = from_char(maze[y][x] + 1);
        cerr << "(" << y << ", " << x << ") " << move << ">>" << next << endl;
        fill_maze(maze, y,     x + 1, next);
        fill_maze(maze, y + 1, x,     next);
        fill_maze(maze, y,     x - 1, next);
        fill_maze(maze, y - 1, x,     next);
    }
    return 0;
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
        string row;
        getline(cin, row);
        cerr << row << endl;
        maze.push_back(row);
        size_t  found = row.find('S');
        if (found != string::npos)
        {
            x = found;
            y = i;
        }
    }
    if (x != -1 && y != -1)
        fill_maze(maze, y, x, 0);

    for (int i = 0; i < h; i++) {

        // Write an answer using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        cout << maze[i] << endl;
    }
}
