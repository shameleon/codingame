#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

    int tx = initial_tx;
    int ty = initial_ty;
    // game loop
    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        // A single line providing the move to be made: N NE E SE S SW W or NW
        string     dir = "";
        
        int delta_y = light_y - ty;
        if (delta_y != 0)
            delta_y = delta_y / abs(delta_y);
        switch (delta_y)
        {
            case -1:
                dir += "N";
                ty--;
                break;
            case 0:
                dir = "";
                break;
            case 1:
                dir += "S";
                ty++;
                break;
        }

        int delta_x = light_x - tx;
        if (delta_x != 0)
            delta_x = delta_x / abs(delta_x);
        switch (delta_x)
        {
            case -1:
                dir += "W";
                tx--;
                break;
            case 0:
                break;
            case 1:
                dir += "E";
                tx++;
                break;
        }
        if (!dir.empty())
            cout << dir << endl;
        else
            cerr << "Error !" << endl;
    }
}