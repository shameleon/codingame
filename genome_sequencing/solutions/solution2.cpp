#include <iostream>
#include <string>
#include <vector>
#include <algorithm> 
using namespace std;

std::string merge_strings(const std::vector< std::string > & pool)
{
	std::string retval;
	for (auto s : pool)
		if (retval.empty())
			retval.append(s);
		else if (std::search(retval.begin(), retval.end(), s.begin(), s.end()) == retval.end())
		{
			size_t len = std::min(retval.size(), s.size());
			for (; len; --len)
				if (retval.substr(retval.size() - len) == s.substr(0, len))
				{
					retval.append(s.substr(len));
					break;
				}
			if (!len)
				retval.append(s);
		}
	return retval;
}

std::string shortest_common_supersequence(std::vector< std::string > & pool)
{
	std::sort(pool.begin(), pool.end());

	std::string buffer;
	std::string best_reduction = merge_strings(pool);
	while (std::next_permutation(pool.begin(), pool.end()))
	{
		buffer = merge_strings(pool);
		if (buffer.size() < best_reduction.size())
			best_reduction = buffer;
	}
	return best_reduction;
}

int main()
{
	int N;
	cin >> N; cin.ignore();
	vector<string> subSequences;
	for (int i = 0; i < N; i++) {
		string subseq;
		cin >> subseq; cin.ignore();
		cerr << subseq << endl;
		subSequences.push_back(subseq);
	}

	string superSequence = shortest_common_supersequence(subSequences);
	cerr << "superSquence: " << superSequence << endl;

	cout << superSequence.size() << endl;
}