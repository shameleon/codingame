#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

/* matching 3'-end of s1 to 5'end of s2 */
string     findSeq(string s1, string s2)
{
    int     i = 0;
    string  sub = s1;
    bool    match_to_s2_5prime = false;
    while (sub.length())
    {
        size_t  found = s2.find(sub);
        if (found!= string::npos)
        {
            cout << sub << " " << found << endl;
            if (!match_to_s2_5prime)
                return s2;
            else if (sub[0] == s2[0])
            {
                string only_s1 = s1.substr(0, i);
                cout << "s1 = " << only_s1 <<  " + " << sub << endl;
                only_s1 += s2;
                return (only_s1);
            }
        }
        match_to_s2_5prime = true;
        sub.erase(0, 1);
        i++;
    }
    return (s1 + s2);
}


void     slide(string s1, string s2)
{
    cout << endl <<  s1 <<  "   " << s2 << endl;
    string res = findSeq(s1, s2);
    cout << res <<  " len= " << res.length() << endl;
    cout << " --------------------------------";
}
int         main()
{
    cout << "sequence match :" << endl;
    slide("AACCC", "GAACTT");       // match=0  len=11
    slide("AACG", "CCTTAACG");    // match=4  len=8
    slide("AAC", "CCTT");         // match=1  len=6
    slide("AACAG", "CAGCTT");     // match=3  len=8
    slide("AAC", "GACTT");        // match=0  len=8
    slide("ATGAGA", "GAGAC");     // match=4  len=7 //
    slide("AAC", "CCTTAAC");      // match=1  len=7
    slide("CCTTAAC", "AAC");      // match=3  len=7
    slide("TGCGA", "GCGATATTAAGCGATAGATA");      // match=3  len=7
    return 0;
}