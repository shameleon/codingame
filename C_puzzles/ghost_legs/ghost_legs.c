#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void     move_to_next_line(char **arr, int i, int j, int col, int W, int H)
{
    if (arr[i][j] == '|')
    {
        if (j >= 3 && arr[i][j - 1] == '-' && arr[i][j - 2] == '-')
            j -= 3;
        else if (j <= (W - 4) && arr[i][j + 1] == '-' && arr[i][j + 2] == '-')
            j += 3;
        move_to_next_line(arr, i + 1, j, col, W, H);
    }
    else
        printf("%c%c\n", arr[0][col], arr[i][j]);
}

void    find_path(char **arr, int W, int H)
{
    int  col = 0;
    while (col < W)
    {
        int i = 1;
        int j = col;
        if (arr[0][col] != ' ')
            move_to_next_line(arr, i, j, col, W, H);
        else
            exit (1);
        col += 3;
    }
}

int     main()
{
    int W;
    int H;
    scanf("%d%d", &W, &H); fgetc(stdin);
    fprintf (stderr, "%d %d\n", W, H);
    //char    arr[H][W];
    char    **arr;
    arr = (char **)malloc (sizeof(*arr) * (H));
    for (int i = 0; i < H; i++) {
        char    buff[1025];
        scanf("%[^\n]", buff); fgetc(stdin);
        arr[i] = strdup(buff);
        fprintf (stderr, "%s\n", arr[i]);
    }
    find_path(arr, W, H);
    return (0);
}