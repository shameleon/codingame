#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    int L;
    scanf("%d", &L);
    int N;
    scanf("%d", &N);
    int left, right;
    left = L;
    right = 0;
    for (int i = 0; i < N; i++) {
        int b;
        scanf("%d", &b);
        fprintf(stderr, "%d ", b );
        if (b < left)
        {
            left = b;
        }
        if (b > right){
            right = b;
        }
    }
    fprintf(stderr, "\nmin=%d max=%d\n", left, right);
    if ( left < L - right)
    {
        printf("%d\n", L - left);
    }
    else
    {
         printf("%d\n", L - L + right);
    }
    return 0;
}