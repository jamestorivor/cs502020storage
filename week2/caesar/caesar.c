#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

char rotate(char c, int i);
bool only_digits(string s);

int main(int argc, string argv[])
{
    //get the key (letting the key be input)
    string input = argv[1];

    //If the key is more than 1 input and not a digit, the it will return 1 and code will not execute
    if (argc != 2 || (!only_digits(input)))
    {
        {
            printf("Usage: ./caesar key\n");
        }
        return 1;
    }

    //Converting input into an int
    int key = atoi(input);

    //getting The plaintext
    string plaintext = get_string("Plaintext: ");

    //converting ciphertext
    printf("Ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n ; i++)
    {
        //Letting x be the variable for the plaintext
        char x = plaintext[i];
        //Rotating plaintext by key
        char cipher = rotate(x, key);
        //Priniting character by character to form a string
        printf("%c", cipher);
    }
    //Printing new line
    printf("\n");
}

//Boolean expression to check if input is an integer or not
bool only_digits(string s)
{
    bool itisadigit;
    for (int i = 0, n = strlen(s); i < n ; i++)
    {
        if (isdigit(s[i]))
        {
            itisadigit = true;
        }
        else
        {
            itisadigit = false;
        }
    }
    return itisadigit;
}

//Conversion of ciphertext function
char rotate(char c, int j)
{
    int f = 0;
    if (isupper(c))
    {
        f = ((c - 65) + j) % 26 + 65;
    }
    else if (islower(c))
    {
        f = ((c - 97) + j) % 26 + 97;
    }
    else
    {
        f = c;
    }
    return f;
}