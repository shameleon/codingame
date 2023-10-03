#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <stack>
using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{



    int l;
    int s;
    int n;
    cin >> l >> s >> n; cin.ignore();
    string prog="";
    for (int i = 0; i < l; i++) {
        string r;
        getline(cin,r);
        prog+=r;
    }
    vector<int> inputs;
    for (int i = 0; i < n; i++) {
        int c;
        cin>>c;
        cin.ignore();
        inputs.push_back(c);
    }

    vector<int> buffer(s,0);
    int pointer = 0;

    vector<bool> valid(prog.size(),false);
    int par = 0;

    vector<int> go(prog.size(),-1);
    stack<int> matches;

    for(int c=0;c<prog.size();c++)
    {
        if(prog[c] == ']'){ 
            if(matches.size() == 0) 
            {
                cout<<"SYNTAX ERROR"<<endl;
                return 0;
            }
            int matche = matches.top(); 
            matches.pop();
            go[matche] = c;
            go[c] = matche-1;
        }
        else if(prog[c]== '[')
        { 
            matches.push(c);
            
        } 
    }
    if(matches.size() > 0)
    {
        cout<<"SYNTAX ERROR"<<endl;
        return 0;
    }

    int index = 0;
    int inputIndex = 0;
    while(index < prog.size())
    {
        if(prog[index] == '>')
        {
            pointer++;
        }
        else if(prog[index] == '<')
        {
            pointer--;
        }
        else if(prog[index] == '+')
        {
            buffer[pointer] += 1;
        }
        else if(prog[index] == '-')
        {
            buffer[pointer] -= 1;
        }
        else if(prog[index] == '.')
        {
            cout<<(char)(buffer[pointer]);
        }
        else if(prog[index] == ',')
        {
            buffer[pointer] = inputs[inputIndex++];
        }
        else if(prog[index] == '[')
        {
            if(buffer[pointer] == 0)
            {
                index = go[index];
            }
        }
        else if(prog[index] == ']')
        {
            if(buffer[pointer] != 0)
            {
                index = go[index];
            }
        }
        if(pointer < 0 || pointer >= buffer.size())
        {
            cout<<"POINTER OUT OF BOUNDS"<<endl;
            return 0;
        }
        if(buffer[pointer] < 0 || buffer[pointer] > 255)
        {
            cout<<"INCORRECT VALUE"<<endl;
            return 0;
        }
        index++;
        
    }
}
