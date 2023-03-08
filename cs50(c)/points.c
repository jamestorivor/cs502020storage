#include <cs50.h>
#include <stdio.h>

int main(void)
{
    const int MINE = 2 ;
    int points = get_int("how many points did you score?\n");

    if (points > mine)
    {
    printf("you scored higher than me!\n");
    }

    else if (points < mine)
    {
    printf("you scored less than me!\n");
    }

    else
    {
    printf("we have the same score!\n");
    }
}