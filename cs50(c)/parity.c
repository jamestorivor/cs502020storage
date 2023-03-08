#include <cs50.h>
#include <stdio.h>

int main(void)

{
    long x = get_long("input your number\n");

    if ( x % 2 == 0)
    {
        printf("even\n");
    }

    else
    {
        printf("odd\n");
    }
}