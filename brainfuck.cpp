# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    brainfuck                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/25 15:49:25 by jmouaike          #+#    #+#              #
#    Updated: 2023/05/25 15:49:43 by jmouaike         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int     l;      // program line count
    int     s;      // s one-byte cells
    int     n;      // integer input

    cin >> l >> s >> n; cin.ignore();
    cerr << l << " " << s << " " << n << endl;
    // s one-byte cells :
    char    c[s];
    for (int i = 0; i < s; i++)
        c[i] = 0;
    for (int i = 0; i < l; i++) {
        string r;
        getline(cin, r);
        cerr <<  r << endl;
        int p = 0;
        for (int k = 0; k < r.length(); k++)
        {
            if (r[k] == '+')
                c[p] += 1;
            else if (r[k] == '.')
                cout << c[p];
            else if (r[k] == '[' && c[p] == 0)
            {
                while (r[k] != ']')
                    k++;
                k++;
            }
            else if (r[k] == '>')
            {
                if (p >= s)
                    runtime_error("POINTER OUT OF BOUNDS");
                p++;
            }
            else if (r[k] == '<')
            {
                if (p >= 0)
                    runtime_error("POINTER OUT OF BOUNDS");
                p--;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c; cin.ignore();
        cerr << c << endl;
    }


    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;
}
