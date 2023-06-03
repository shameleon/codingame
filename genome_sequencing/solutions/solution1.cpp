#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int N, i=0; cin >> N;
    vector<string> seqs(N);
    vector<int>    perm;
    string         shortest = "";
	for (auto &s:seqs) cin >> s, shortest += s, perm.push_back(i++);
    do {
        string seq = seqs[perm[0]];
        for (int i=1; i<N; i++) if (seq.find(seqs[perm[i]]) == -1){
            int best = 0;
			int num = min(seq.size(), seqs[perm[i]].size());
            for (int j=1; j<num; j++){
                string first  = seq.substr(seq.size() - j);
                string second = seqs[perm[i]].substr(0, j);
                if (first == second) best = j;
            }
            seq += seqs[perm[i]].substr(best);
        }
        if (seq.size() < shortest.size()) shortest = seq;
    } while (next_permutation(perm.begin(), perm.end()));
    cout << shortest.size() << endl;
}