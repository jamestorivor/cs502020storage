#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int n;
    do
    {
        n = get_int("Number of bricks:");
    }
    while (n < 1);

    {
    for (int x = 0; x < n; x++)
        {
        for (int y = 0 ; y < n; y++)
            {
            printf ("#");
            }
        printf("\n");
        }
    }
}