// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = (LENGTH * 'z') + 1;

// Hash table
node *table[N];

//Number of words from load
int number_of_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int integer = hash(word);
    for (node *tmp = table[integer]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(tmp->word, word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //add all the letters in the word and create a bucket for each
    int word_sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        word_sum += tolower(word[i]);
    }
    return (word_sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    //create character array to store words
    char storage[LENGTH + 1];

    while (fscanf(file, "%s", storage) != EOF)
        //Read strings from a file
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        //get hash value of word
        int integer = hash(storage);
        //copy word from character array into node
        strcpy(n->word, storage);
        //check if bucket has been used
        if (table[integer] == NULL)
        {
            n->next = NULL;
            table[integer] = n;
        }
        else
        {
            n->next = table[integer];
            table[integer] = n;
        }
        number_of_words++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return number_of_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            return false;
        }
    }
    return true;
}
