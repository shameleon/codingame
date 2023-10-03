#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

#define WCODE "janfebmaraprmayjunjulaugsepoctnovdec"

int     identify_word(char *w)
{
    int     n;
    int     i;

    n = 0;
    while (n < 12)
    {
        if((WCODE[n * 3] == w[0]) && (WCODE[n * 3 + 1] == w[1]) 
            && (WCODE[n * 3 + 2] == w[2]))
            return (n);
        n++;
    }
    return (n);
}

void    parse_address(char *s)
{
    int i;

    i = 0;
    while (s[i])
    {
        if (s[i] != ' ')
        {
            int d = identify_word((s + i));
            int n = identify_word((s + i + 3));
            if (d == 12 || n == 12)
                fprintf(stderr, "ERROR : code not found\n");
            else
                printf("%c", d * 12 + n);
            i += 6;
        }
        else
            i++;
    }
}

int time_to_int(char *time)
{
    int nb;
    int m;
    int i;

    nb = 0;
    i = 0;
    while (time[i])
        i++;
    i--;
    m = 1;
    while (i >= 0)
    {
        if (time[i] == '#')
            nb += m;
        m *= 2;
        i--;
    }
    return(nb);
}

void    print_time(char *time)
{
    int decrypted_time = time_to_int(time);
    int hours = decrypted_time / 100;
    int min = decrypted_time % 100;
    printf("%02d:%d\n", hours, min);
}
int main()
{
    char time[33];
    scanf("%[^\n]", time); fgetc(stdin);
    char address[2049];
    scanf("%[^\n]", address);

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n")
    print_time(time);
    parse_address(address);
    return (0);
}
