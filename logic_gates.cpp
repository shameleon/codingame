/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   logic_gates.cpp                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jmouaike <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/25 09:19:27 by jmouaike          #+#    #+#             */
/*   Updated: 2023/05/25 11:22:07 by jmouaike         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

#include <iostream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

typedef struct  s_output
{
    string  name;
    string  type;
    string  input_name_1;
    string  input_name_2;
    string  signal;
}               t_output;

enum            e_operate
{
    AND,
    OR,
    XOR,
    NAND,
    NOR,
    NXOR,
};


char        operate_char(int type_index, char c1, char c2)
{
    char res;
    switch (type_index)
    {
        case AND:
            res = (c1 == '-' && c2 == '-') ? '-' : '_';
            break;
        case OR:
            res = (c1 == '-' || c2 == '-') ? '-' : '_';
            break;
        case XOR:
            res = ((c1 == '-' && c2 == '_') || (c1 == '_' && c2 == '-')) ? '-' : '_';
            break;
        case NAND:
            res = (c1 == '-' && c2 == '-') ? '_' : '-';
            break;
        case NOR:
            res = (c1 == '-' || c2 == '-') ? '_' : '-';
            break;
        case NXOR:
            res = ((c1 == '-' && c2 == '-') || (c1 == '_' && c2 == '_')) ? '-' : '_';
            break;
        default:
            res = '\0';
    }
    return res;
}

string    operate_string(string const &type, string const &str1, string const &str2)
{
    map<string, int>                operations = {{"AND", AND}, {"OR", OR}, {"XOR", XOR},
                                                {"NAND", NAND}, {"NOR", NOR}, {"NXOR", NXOR}};
    map<string, int>::iterator      it = operations.find(type);
    string                          output = "";
    int                             type_index = it->second;

    for (int k = 0; k < str1.length() && k < str2.length(); k++)
        output += operate_char(type_index, str1[k], str2[k]);
    return output;
}

int main()
{
    int n;
    cin >> n; cin.ignore();
    int m;
    cin >> m; cin.ignore();
    map<string, string>     input;
    for (int i = 0; i < n; i++) {
        string      input_name, input_signal;
        cin >> input_name >> input_signal; cin.ignore();
        input.insert(pair<string, string>(input_name, input_signal));
    }
    cerr << "A " << input["A"] << endl;
    cerr << "B " << input["B"] << endl;
    t_output    output[m];
    for (int i = 0; i < m; i++) {
        cin >> output[i].name >> output[i].type >> output[i].input_name_1 >> output[i].input_name_2;
        cin.ignore();
        map<string, string>::iterator       it1, it2;
        string str1, str2;
        it1 = input.find(output[i].input_name_1);
        str1 = it1->second;
        it2 = input.find(output[i].input_name_2);
        str2 = it2->second;
        output[i].signal = operate_string(output[i].type, str1, str2);
    }

    for (int i = 0; i < m; i++) {
        // Write an answer using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        cout << output[i].name << " " << output[i].signal << endl;
    }
}

