#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    string lon;
    cin >> lon; cin.ignore();
    string lat;
    cin >> lat; cin.ignore();
    int n;
    cin >> n; cin.ignore();
    cerr << lon << " " << lat << "   n=" << n << endl;
    for (int i = 0; i < n; i++) {
        string defib, field;
        getline(cin, defib);
        stringstream    ss(defib);
        while (field)
        {           
            getline(ss, field, ';');
            cerr << field << endl;
        }
    }


    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "answer" << endl;
}
