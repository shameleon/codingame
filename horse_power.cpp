/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   horse_power.cpp                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/24 13:12:48 by jmouaike          #+#    #+#             */
/*   Updated: 2023/05/24 13:12:52 by jmouaike         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int     abs_diff(vector<int>::iterator first, vector<int>::iterator second)
{
    int                         diff;

    diff = abs(*first - *second);
    return diff;
}

int main()
{
    int                         n;
    cin >> n; cin.ignore();
    vector<int>                 horses_pi;

    for (int i = 0; i < n; i++)
    {
        int pi;
        cin >> pi; cin.ignore();
        horses_pi.push_back(pi);
    }
    sort(horses_pi.begin(), horses_pi.end());

    vector<int>::iterator       best_pair;
    vector<int>::iterator       start = horses_pi.begin();
    int                         smallest_diff =  10000001;

    for(vector<int>::iterator it = start; it != horses_pi.end() - 1; ++it)
    {
        int     diff = abs_diff(it , it + 1);
        if (it == start || diff < smallest_diff)
        {
            best_pair = it;
            smallest_diff = diff;
        }
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << smallest_diff << endl;
}
