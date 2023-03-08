#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


char rotate( char c, int i);
int main (void)
{
 string input = get_string("type here: ");
 int number = get_int("Key: ");
   for ( int i = 0, n = strlen(input); i < n ; i++)
        {
        char e = input[i];
        char g = rotate( e , number );
        printf("%c", g );
        }
        printf("\n");
}






char rotate( char c, int i )
{
        char f = 0;
        if (isupper(c))
        {
         f = ( (c - 65) + i )%26 + 65;
        }
        else if (islower(c))
        {
         f =  ( (c - 97) + i )%26 + 97;
        }
return f;
}