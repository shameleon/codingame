#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/* progress 100% */

int     getMaxLoss(vector <int> &val)
{
    vector <int>::iterator  hi = val.begin();
    vector <int>::iterator  low = val.begin();
    int result = 0;

    for(vector <int>::iterator it = val.begin() + 1; it != val.end(); ++it)
    {
        if (*it < *hi)
        {
            if (*it < *low)
                low = it;
        }
        else
        {
            result = min(result, *low - *hi);
            hi = it;
            low = hi;
        }
    }
    result = min(result, *low - *hi);
    return result;
}

int main()
{
    int n;
    cin >> n; cin.ignore();
    vector <int>  val;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v; cin.ignore();
        val.push_back(v);
    }
    cerr << endl;
    int answer = getMaxLoss(val);
    cout << answer << endl;
}

