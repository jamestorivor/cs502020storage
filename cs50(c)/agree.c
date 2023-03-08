#include <cs50.h>
#include <stdio.h>

int main(void)

{
    {
        printf( "please input y for yes and n for no\n" );
    }
    char ans = get_char("Are you full? \n");

    //Input for yes
    if (ans == 'y' || ans == 'Y')
    {
        printf("Okay stop eating then. \n");
    }

    //Input for no
    if (ans == 'n' || ans == 'N')
    {
        printf("Eat more then.\n");
    }
}