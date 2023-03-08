#include <stdio.h>
#include <cs50.h>

int main(void)

{
        int n ;
        do
        {
            n = get_int("Width: ");
        }
        while (n < 1);

    for (int x = 0; x < n ; x++)
    {
        printf("?");
    }

    {
        printf("\n");
    }
}