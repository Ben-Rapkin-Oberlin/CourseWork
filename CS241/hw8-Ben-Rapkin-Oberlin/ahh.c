#include <stdio.h>
#include <stdlib.h>


void BinaryToText(char *inputFile, char *outputFile)
{
    unsigned char str[256];
    unsigned int num; // assuming 32 bit ints
    int len;

    FILE *finp = fopen(inputFile, "rb");
    FILE *fout = fopen(outputFile, "w");

    while ((len = fgetc(finp)) != EOF)
    {
        fread(str, len, 1, finp);
        str[len] = '\0';
        num = (unsigned int)fgetc(finp) << 24;
        num |= fgetc(finp) << 16;
        num |= fgetc(finp) << 8;
        num |= fgetc(finp);
        fprintf(fout, "%s\n", (char *)str);
    }
    fclose(finp);
    fclose(fout);
}

void ReadFile(char *name)
{
    FILE *file;
    char *buffer;
    unsigned long fileLen;

    // Open file
    file = fopen(name, "rb");
    if (!file)
    {
        fprintf(stderr, "Unable to open file %s", name);
        return;
    }

    // Get file length
    fseek(file, 0, SEEK_END);
    fileLen = ftell(file);
    fseek(file, 0, SEEK_SET);
    
    // Allocate memory
    buffer = (char *)malloc(fileLen + 1);
    if (!buffer)
    {
        fprintf(stderr, "Memory error!");
        fclose(file);
        return;
    }

    // Read file contents into buffer
    fread(buffer, fileLen, 1, file);
    fclose(file);
    buffer[fileLen+1]='\0';
    for (long unsigned int i = 0; i < fileLen + 1; i++)
    {
        printf("%i\n", buffer[i]);
    }

    free(buffer);
}

void convertBin(char *name)
{
    FILE *file;
   // char *buffer;
    unsigned long fileLen;

    // Open file
    file = fopen(name, "rb");
    if (!file)
    {
        fprintf(stderr, "Unable to open file %s", name);
        return;
    }
    char buffer[11];
    for (int i=0; i<11; i++){
        char a=fgetc(file);
    	//printf("num: %u \n",a);  	
	    buffer[i]=a;
    }
    fclose(file);
    FILE *fout = fopen("temp.txt", "w");

    for (int i=0; i<11; i++){
      for(int bit=0;bit<8; bit++)
        {   
            fprintf(fout, "%i", buffer[i] & 0x01);
             buffer[i] =  buffer[i] >> 1;
        }
    }
    fclose(fout);
}
