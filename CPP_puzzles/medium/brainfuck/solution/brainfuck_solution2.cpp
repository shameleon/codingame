#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int lines, size, inputs, ptr_pos = 0;
    cin >> lines >> size >> inputs; cin.ignore();
    int array[size] = {0};
    string command;
    for (int i = 0; i < lines; i++)
    {
        string str; getline(cin, str); command += str;
    }
    string result;
    if (count(command.begin(), command.end(), '[')
    != count(command.begin(), command.end(), ']'))
        result = "SYNTAX ERROR";
    else for (int i = 0; command[i]; ++i)
    {
        if (command[i] == '>')
            ++ptr_pos;
        else if (command[i] == '<')
            --ptr_pos;
        else if (command[i] == '+')
            ++array[ptr_pos];
        else if (command[i] == '-')
            --array[ptr_pos];
        else if (command[i] == '.')
            result += (char)array[ptr_pos];
        else if (command[i] == ',')
        {   
            cin >> array[ptr_pos]; cin.ignore();
        }
        int b = 1;
        if (command[i] == '[' && array[ptr_pos] == 0)
        {
            while (b && ++i < size)
                if (command[i] == '[')
                    ++b;
                else if (command[i] == ']')
                    --b;
            ++i;
        }
        else if (command[i] == ']' && array[ptr_pos] != 0)
        {
            while (b && --i >= 0)
                if (command[i] == ']')
                    ++b;
                else if (command[i] == '[')
                    --b;
            --i;
        }
        if (ptr_pos < 0 || ptr_pos >= size)
        {
            result = "POINTER OUT OF BOUNDS";
            break;
        }
        if (array[ptr_pos] < 0 || array[ptr_pos] > 255)
        {
            result = "INCORRECT VALUE";
            break;
        }
    }
    cout << result;
}
