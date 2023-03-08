#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentence(string text);

int main(void)
{
    string input = get_string("Text: ");
    //Converting input into number of words, letters and sentences
    int letters = count_letters(input);
    int words = count_words(input);
    int sentences = count_sentence(input);
    //Average number of letters per 100 words
    float L = 100 * ((float)letters / words);
    //Average number of sentences per 100 words
    float S = 100 * ((float)sentences / words);
    //Formula for calculating grade level
    float index = 0.0588 * L - 0.296 * S - 15.8;
    //Printing of Grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int)round(index));
    }
}

//Function for counting number of sentences
int count_sentence(string text)
{
    int counted = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            counted++;
        }
    }
    return counted;
}

//Function for counting number of words
int count_words(string text)
{
    int n = strlen(text);
    int counting = 0;
    if (n > 0)
    {
        for (int i = 0; i < n; i++)
        {
            //calculating number of words by using the number of spaces in a sentence
            if (isspace(text[i]))
            {
                counting++;
            }
        }
        //Return + 1 due to number of spaces being one less than number of words
        return counting + 1;
    }
    //if no input, number of words = 0 not 1
    else
    {
        return counting = 0;
    }
}

//Function for counting number of letters
int count_letters(string text)
{
    int counter = 0;
    for (int i = 0, n = strlen(text); i < n ; i++)
    {
        if (isalpha(text[i]))
        {
            counter += 1;
        }
    }
    return counter;
}