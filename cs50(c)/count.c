#include <cs50.h>
#include <stdio.h>



int main(void)
{

    int n = get_int("number of scores: ");

    int scores[n];

    int score = 0;

    for( int j = 0; j < n ; j++)
    {
            scores[j] = get_int("score: ");
            score += scores[j];
    }

    int y = (score / n);

    printf("average : %d\n" , y) ;
}



