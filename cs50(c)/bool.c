#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>


bool only_digits(string s);
int main(void)
{
    string n = get_string("Input a number:");
if ( strlen(n) != 2 || only_digits(n) == true)
{
    printf("hi");
}
else
{
    printf("bye");
}
}

bool only_digits(string s)
{
    int temp = 0;
    bool yesdigit = temp;
    for ( int i = 0, n = strlen(s); i < n ; i++)
    if (isdigit(s[i]))
    {
        return true;
    }
    else
    {
        return false;
    }

    return temp;
}