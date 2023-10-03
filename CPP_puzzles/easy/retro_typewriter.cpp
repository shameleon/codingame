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

void    parse_and_display_chunk(string str, int repeats)
{
    string        obj = "";
    string        abbrev[] = {"sp", "bS", "sQ", "nl"};
    char          display[] = {' ', '\\', '\'', '\n'};
    size_t        found[4];

    for (int i =0; i < 5; i++)
    {
        if (i < 4){
            found[i] = str.find(abbrev[i]); 
            if (found[i] != string::npos)
            {
                obj +=  display[i];
                if (i == 3)
                    repeats = 1;
                break;
            }
        }
        else
        {
            int last = str.length() - 1;
            obj += str[last];
            if (isdigit(obj[0]))
                repeats /= 10;
        }
    }
    for (int i = 0; i < repeats; i++)
        cout << obj[0];
}

int main()
{
    string              t;
    getline(cin, t);
    cerr << t << endl;
    stringstream       iss(t);
    do
    {
        string          chunk;
        iss >> chunk;
        int repeats;
        stringstream       ss(chunk);
        ss >> repeats;
        if (chunk.length())
            parse_and_display_chunk(chunk, repeats);
    }
    while (iss);

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
}

 
/*
 *some solutions : 

 * map<string, char> abbr = {{"sp", ' '}, {"bS", '\\'}, {"sQ", '\''}, {"nl", '\n'}};
 * if (t.compare("nl") == 0) {cout << endl; break;};
 * int n = stoi(t.substr(0, i));
 *                    string s = t.substr(i+1, t.size());
                    if (abbr.find(s) != abbr.end()) {
                        char c = abbr.find(s)->second;
 ***************
 *
 * std::regex rg("(\\d+)(.+)");
            std::smatch smInfo;
            if(std::regex_match(blockToDraw, smInfo, rg) == true)
            {
                const int nbOccurences = stoi(smInfo[1]);
                std::string carToAdd = smInfo[2];

		**********************

		#include <iostream>
using namespace std;
int main(){
  string s,r,t,u;
  while(cin>>s){
    int x=size(s)-2;
    t=s.substr(x,2),u=s.substr(0,x);
    r=s.back(),s.pop_back();
    if(t=="sp")r=" ",s=u;
    if(t=="bS")r=92,s=u;
    if(t=="sQ")r=39,s=u;
    if(t=="nl")r=10,s="1";
    for(int i=0;i<stoi(s);i++)cout<<r;}}
 *
 * */
