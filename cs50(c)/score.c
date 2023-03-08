#include <stdio.h>
#include <cs50.h>

int compute_avg(int number);

int main(void)
{
    //number of inputs
    int input1 = get_int("How many scores User 1: ");
        int User1 = compute_avg(input1);
    int input2 = get_int("How many scores User 2: ");
       int User2 = compute_avg(input2);

    //Printing the scores
    printf("Average for User 1 :%d\n", User1 );
    printf("Average for User 2 :%d\n", User2 );

    //Comparing results:
    if (User1 > User2)
    {
        printf("User 1 with an average of %d did better than User 2 with an average of %d\n", User1, User2);
    }
    else if (User2 > User1)
    {
        printf("User 2 with an average of %d did better than User 1 with an average of %d\n", User2, User1);
    }
    else
    {
        printf("User 1 and 2 have the same average of %d", User1);
    }
    {
        printf("\n");
    }
}

int compute_avg(int number)
{
    int score = 0;
    int scores[number];
    for ( int i = 0; i < number ; i++)
    {
        scores[i]= get_int("score: ");
        score += scores[i];
    }
    return score;

    int x = (score / number);
}