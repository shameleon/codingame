#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

/* try to find s1 inside s2
then matching s1 3'-end to s2 5'-end 
*/
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
            if (!match_to_s2_5prime)
                return s2;
            else if (found == 0)                //sub[0] == s2[0])
                return (s1.substr(0, i) + s2);
        }
        match_to_s2_5prime = true;
        sub.erase(0, 1);
        i++;
    }
    return (s1 + s2);
}


int    match(string s1, string s2)
{
    string res = findSeq(s1, s2);
    cout << setw(10) << s1.length() + s2.length() - res.length();
    return (s1.length() + s2.length() - res.length());
}

int     main()
{
    vector<string>      seq;

 /*   seq.push_back("AATGAACGGC");
    seq.push_back("GCAACGGCAATG");  
    seq.push_back("CGGCAATGAATTAG");
    seq.push_back("TGTTATTAAATGAA");
    seq.push_back("GATTTCAAATTTGTT");
    cout << endl;
 */
    seq.push_back("CCCTG");
    seq.push_back("TGAACA");
    seq.push_back("CATGA");  
    // adjacency matrix
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (i == j)
                cout << setw(10) << "-";
            else
                match(seq[i], seq[j]);
        }
        cout << endl;
    }
    // 0>1>2>0 clockwise
    int cw_sum = 0;
    for (int i = 0; i < 3; i++)
    {
        int j = (i + 1) % 3;
        cw_sum += match(seq[i], seq[j]);
    }
    cout << endl << cw_sum << endl;
    // keep best 2

    // 0>2>1>0 clockwise
    int ccw_sum = match(seq[0], seq[2]);
    ccw_sum += match(seq[2], seq[1]);
    ccw_sum += match(seq[1], seq[0]);

    cout << endl << ccw_sum << endl;

}
/*
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
    slide("TGCGA", "GCGATATTAAGCGATAGATA");      // match=34  len=21
    return 0;
}

*/