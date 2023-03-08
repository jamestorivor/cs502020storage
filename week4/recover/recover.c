#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

//Open memory card
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file %s\n", argv[1]);
        return 2;
    }
//Repeat reading till end of card;
//Create buffer
    BYTE buffer[512];
//read 512 bytes into a buffer
    const int BLOCK_SIZE = 512;
    FILE *img = NULL;
    int counter = 0;
    //Transfer from file to buffer
    while (fread(&buffer, BLOCK_SIZE, 1, file) == 1)
    {
        char filename[8];
        //if start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //Open new JPEG file
            //If first JPEG
            if (counter == 0)
            {
                //Copy from buffer to each jpg file
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                counter++;
            }
            //Else
            else if (counter > 0)
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                counter++;
            }
        }
        //Else
        if (counter > 0)
        {
            //If already found JPEG
            fwrite(&buffer, BLOCK_SIZE, 1, img);
        }
    }
    fclose(img);
    fclose(file);
}