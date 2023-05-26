/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   conway_suite.cpp                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/26 15:55:48 by jmouaike          #+#    #+#             */
/*   Updated: 2023/05/26 15:56:01 by jmouaike         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int             r;
    cin >> r; cin.ignore();
    int             l;
    cin >> l; cin.ignore();

    // init
    int             line_number = 0;
    deque<int>      line;

    line.push_back(r);
    while(++line_number < l)
    {
        deque<int>      newline;
        
        while (!line.empty())
        {
            int             count = 1;
            int             val = line.front();
            line.pop_front();
            while(val == line.front())
            {
                count++;
                line.pop_front();
            }
            newline.push_back(count);
            newline.push_back(val);
        }
        line = newline;

    }
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    for(deque<int>::iterator it = line.begin(); it != line.end(); ++it)
    {
        cout << *it;
        if (it < line.end() - 1)
            cout << " ";
    }
    return 0;
}

