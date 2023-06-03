#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>
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

int    align_permutation(vector<string> &seq)
{
	string  s = seq[0];
	for (unsigned long i = 1; i < seq.size(); i++){
		cerr << s << " + " << seq[i] << endl;
		s = findSeq(s, seq[i]);
	}
	cerr << s << endl;
	cerr << s.length() << endl;
	return (s.length());
}

int		main()
{
	vector<string>		input;

 /*   seq.push_back("AATGAACGGC");
	seq.push_back("GCAACGGCAATG");  
	seq.push_back("CGGCAATGAATTAG");
	seq.push_back("TGTTATTAAATGAA");
	seq.push_back("GATTTCAAATTTGTT");
	cout << endl;
 */
	input.push_back("CCCTG");
	input.push_back("TGAACA");
	input.push_back("CATGA");

	vector<string>		seq;
	seq.push_back("CCCTG");
	seq.push_back("TGAACA");
	seq.push_back("CATGA");
	sort(seq.begin(), seq.end());
	
	vector<int>         res; 
 
    do res.push_back(align_permutation(seq));
    while (next_permutation(seq.begin(), seq.end()));

	vector<int>::iterator shortest_seq = min_element(res.begin(), res.end());
	cout << *shortest_seq;
}
