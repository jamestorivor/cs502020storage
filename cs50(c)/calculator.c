#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Prompt user for x
    float x = get_float("x: ");

    //Prompt user for y
    float y = get_float("y: ");

    float z = ( x / y );

    //Perform addition
    printf("%.2f\n", z );
}