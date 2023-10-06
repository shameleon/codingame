#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/* First, if s1 is found inside s2.
then if s1 3'-end matches to s2 5'-end */
string     findSeq(string const s1, string const s2)
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

/*  Sequential alignment of a given permutation of sequences.
returning the length of the resulting aligned sequence */
int    align_permutation(vector<string> &seq)
{
	string  s = seq[0];
	for (unsigned long i = 1; i < seq.size(); i++)
		s = findSeq(s, seq[i]);
	return (s.length());
}

int main()
{
    int n;
    cin >> n; cin.ignore();
    vector< string >       seq;
    string              subseq;
    for (int i = 0; i < n; i++) {
        cin >> subseq; cin.ignore();
        cerr << subseq << endl;
        seq.push_back(subseq);
    }

    sort(seq.begin(), seq.end());	
	vector<int>         res; 
    do res.push_back(align_permutation(seq));
    while (next_permutation(seq.begin(), seq.end()));
	vector<int>::iterator shortest_seq = min_element(res.begin(), res.end());
	cout << *shortest_seq << endl;
}
