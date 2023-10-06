#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void		match(string &str1, string &str2)
{
	string		res =  "";

	for (size_t i = 0; i < str2.length(); ++i)
	{
		cout << (str1[i] == str2[i]);
	}
	cout << res << endl;
}

void		slide(string s1, string s2)
{
	string	str1 = s1;
	string	str2 = s2;

	str1.insert(str1.end(), s2.length(), '.');
	str2.insert(str2.begin(), s1.length(), '.');
	cout << str1 << endl;
	cout << str2 << endl;
	match(str1, str2);
	while (str2[0] == '.')
	{
		str2.erase(0, 1);
		cout << str2 << endl;
		match(str1, str2);
		cout << endl;
	}
}

int         main()
{
	cout << "sequence slider :" << endl;
	slide("AAC", "CCTT");         // match=1  len=6
	slide("AACAG", "CAGCTT");     // match=3  len=8
	slide("AAC", "GACTT");        // match=0  len=8
	slide("AAC", "GAACTT");       // match=3  len=9
	slide("ATGAGA", "GAGAC");     // match=4  len=7  //
	slide("AAC", "CCTTAAC");      // match=1  len=9
	// slide("C", "C");              // match=1  len=1
	// slide("C", "A");              // match=0  len=2
	return 0;
}