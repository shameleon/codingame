#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int     is_valid_number(char  *str)
{
    int         sum1;
    int         sum2;
    int         second_digits[8] = {17, 15, 12, 10, 7, 5, 2, 0};
    
    sum1 = 0;
    sum2 = 0;
    for (int i = 0; i < 8; i++)
    {
        char    c;

        c = str[second_digits[i]];
        if (c < '0' || c > '9')
            return (0);
        sum2 += (2 * (c - '0')) / 10 + (2 * (c - '0')) % 10;
        c = str[second_digits[i] + 1];
        if (c < '0' || c > '9')
            return (0);
        sum1 += c - '0';
    }
    fprintf(stderr, "%d\t", sum2);
    fprintf(stderr, "%d\n\n", sum1);
    return ((sum2 + sum1) % 10);
}

int main()
{
    int     n;
    int     *res;

    res = (int *)malloc(sizeof(*res) * n);
    if (!res)
        return (1);
    scanf("%d", &n); fgetc(stdin);
    fprintf(stderr, "%d\n", n);
    for (int i = 0; i < n; i++) {
        char card[21];
        scanf("%[^\n]", card); fgetc(stdin);
        fprintf(stderr, "%s\n", card);
        res[i] = is_valid_number(card);
    }
    for (int i = 0; i < n; i++) {
        if (res[i] == 0) 
            printf("YES\n");
        else
            printf("NO\n");
    }
    free (res);
    return (0);
}