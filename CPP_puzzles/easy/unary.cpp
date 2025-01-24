#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    string message;
    getline(cin, message);

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
    vector<int>     bytes;

    // parsing message string
    for (int i = 0; i < message.length(); ++i)
    {
        int     c = static_cast<int>(message[i]);
        int     n = 64;

        // fill bits
        for (int j = 0; j < 7; j++)
        {
            bytes.push_back(c / n);
            c = c % n;
            n /= 2;
        }
    }

    vector<int>::iterator it = bytes.begin();
    while (it != bytes.end())
    {
        switch (*it)
        {
            case 0:
                cout << "00 ";
                while (*it == 0 && it < bytes.end())
                {
                    cout << "0";
                    it++;
                }
                it--;
                break;
            case 1:
                cout << "0 ";
                while (*it == 1 && it < bytes.end())
                {
                    cout << "0";
                    it++;
                }
                it--;
                break;  
            default:
                cerr << "Error" << endl;               
        }
        if (it < bytes.end() - 1)
            cout << " ";
        it++;
    }
    return 0;
}

