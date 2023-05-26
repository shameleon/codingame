/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Le_cadeau.cpp                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/26 11:40:40 by jmouaike          #+#    #+#             */
/*   Updated: 2023/05/26 11:40:49 by jmouaike         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int    ifsum_vec(vector<int> &vec, int &m, int threshold)
{
    int     ifsum = 0;
    for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
    {
        if (*it < threshold)
        {
            ifsum += *it;
            m++;
        }
    }
    return ifsum;
}

int    sum_vec(vector<int> &vec)
{
    int     sum = 0;
    for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
        sum += *it;
    return sum;
}

void    optimize_contributions(vector<int> &vec, int const c, int const n)
{
    int                     sum = sum_vec(vec);
    vector<int>::iterator   it = vec.end() - 1;
    int                     m = 0;

    // counting m contributions under c / n threshold with a total amount is m_sum
    int                     m_sum = ifsum_vec(vec, m, c / n);
    cerr << "m_sum=" << m_sum << " m=" << m << endl;

    // (n - m) paticipants have now to contibute up to (c - m_sum)
    while (n > m && sum != c)
    {
        if (*it > (c - m_sum) / (n - m))
        {
            *it -= 1;
            sum--;
        }
        else
            it--;
    }
    sort(vec.begin(), vec.end());
}

int     main()
{
    int n;
    cin >> n; cin.ignore();
    int c;
    cin >> c; cin.ignore();
    vector<int> vec;

    cerr << "input: ";
    for (int i = 0; i < n; i++)
    {
        int b;
        cin >> b; cin.ignore();
        cerr << b << " ";
        vec.push_back(b);
    }
    cerr << endl << c << endl;
    sort(vec.begin(), vec.end());
    int sum = sum_vec(vec);
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    if (sum < c)
        cout << "IMPOSSIBLE" << endl;
    else
    {
        if (sum != c)
            optimize_contributions(vec, c, n);
        cerr << "output: ";
        for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
            cerr << *it << " ";
        cerr << endl;
        for (vector<int>::iterator it = vec.begin(); it != vec.end(); ++it)
            cout << *it << endl;
    }
}
