#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    char *p = &s[0];
    printf("output: %c\n", *p);
    printf("output: %c\n", *(p + 1));
    printf("output: %c\n", *(p + 2));
}