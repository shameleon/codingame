#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

/* tests ok */
void     slide(string s1, string s2)
{
    string::iterator        it2, it2r;

    for (it2 = s2.begin() ; it2 < s2.end(); ++it2)
        if (*it2 == *(s1.end() - 1) )
            break;


    for (it2r = s2.end() - 1 ; it2r < s2.begin(); ++it2r)
        if (*it2r == *(s1.end() - 1) )
            break;

    //int index = it2 - s2.begin();
    string::iterator    it2p = s2.begin();
    string::iterator    it1 = (s1.end() - 1) - (it2 - s2.begin());
    int    match = 0;
    
    while( *it1 == *it2p && it1 < s1.end())
    {
        match += 1;
        it1++;
        it2p++;
    }
    cerr << "match " << match << "  ";
    int new_size = s1.size() + s2.size() - match;
    cout << "final_size " << new_size << endl;
}

int         main()
{
    cout << "sequence slider :" << endl;
    slide("AAC", "CCTT");         // match=1  len=6
    slide("AACAG", "CAGCTT");     // match=3  len=8
    slide("AAC", "GACTT");        // match=0  len=8
    slide("AAC", "GAACTT");       // match=0  len=9
    slide("ATGAGA", "GAGAC");     // match=4  len=7 //
    slide("AAC", "CCTTAAC");      // match=1  len=9
    slide("CCTTAAC", "AAC");      // match=3  len=7
    slide("C", "C");              // match=1  len=1
    slide("C", "A");              // match=0  len=2
    return 0;
}