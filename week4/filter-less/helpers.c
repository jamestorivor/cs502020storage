#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //looping through all the pixels
    for (int i = 0, n = height; i < n ; i++)
    {
        for (int j = 0, o = width; j < o ; j++)
        {
            //calculate average of the BRG values
            float average = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0;
            int number = round(average);
            //implementing the average values to each BGR value
            image[i][j].rgbtGreen = image[i][j].rgbtBlue = image[i][j].rgbtRed = number;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, n = height; i < n ; i++)
    {
        for (int j = 0, o = width; j < o ; j++)
        {
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            int cRed = round(sepiaRed);
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            int cGreen = round(sepiaGreen);
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            int cBlue = round(sepiaBlue);
            image[i][j].rgbtRed = cRed;
            image[i][j].rgbtGreen = cGreen;
            image[i][j].rgbtBlue = cBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0, n = height; i < n ; i++)
    {
        for (int j = 0, o = width; j < o / 2; j++)
        {
            //Swapping Red
            BYTE *p = &image[i][j].rgbtRed;
            BYTE *z = &image[i][o - (j + 1)].rgbtRed;
            int tmp = *p;
            *p = *z;
            *z = tmp;
            //Swapping Green
            BYTE *a = &image[i][j].rgbtGreen;
            BYTE *b = &image[i][o - (j + 1)].rgbtGreen;
            int tamp = *a;
            *a = *b;
            *b = tamp;
            //Swapping Blue
            BYTE *c = &image[i][j].rgbtBlue;
            BYTE *d = &image[i][o - (j + 1)].rgbtBlue;
            int temp = *c;
            *c = *d;
            *d = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, o = width; j < o; j++)
        {
            //Copying image to copy
            copy[i][j] = image[i][j];
        }
    }
//Initializing vairables
    for (int i = 0, n = height; i < n; i++)
    {
        for (int j = 0, o = width; j < o; j++)
        {
            float sumRed;
            float sumGreen;
            float sumBlue;
            int counter;
            counter = sumBlue = sumRed = sumGreen = 0;
            //Use a nested for loop to iterate a 3x3 box which skips over any pixel outside of the image. Initialize variables and set RGB values.
            //3 Rows for the 3x3 box, from i-1 to i+1
            for (int k = i - 1 ; k < i + 2 ; k++)
            {
                //3 columns for the 3x3 box, from j-1 to j+1
                for (int r = j - 1 ; r < j + 2; r++)
                {
                    //If outside the image, continue
                    if (k < 0 || k > n - 1 || r < 0 || r > o - 1)
                    {
                        continue;
                    }
                    //If in the image, add the value and increase counter
                    else
                    {
                        sumRed += copy[k][r].rgbtRed;
                        sumGreen += copy[k][r].rgbtGreen;
                        sumBlue += copy[k][r].rgbtBlue;
                        counter++;
                    }
                }
            }
            //Average of RGB values to return to image
            image[i][j].rgbtRed = round(sumRed / counter);
            image[i][j].rgbtBlue = round(sumBlue / counter);
            image[i][j].rgbtGreen = round(sumGreen / counter);
        }
    }
    return;
}
