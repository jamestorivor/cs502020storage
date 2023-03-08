#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompting for input
    int input;
    do
    {
        input = get_int("Height: ");
    }
    while (input < 1 || input > 8);

    //Print stairs
    {
        for (int loop = 0 ; loop < input ; loop++)
        {
            //Printing invsible backward steps
            for (int i = 0 ; i < input - (loop + 1) ; i++)
            {
                printf(" ");
            }
            //Printing visible LHS steps
            for (int i = 0 ; i < loop + 1 ; i++)
            {
                printf("#");
            }
            printf("\n");
        }
    }
}

