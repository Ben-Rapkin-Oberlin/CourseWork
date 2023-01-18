#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>   
#include <ctype.h>
#include "qs.h"
const int MAX_LINES = 1048576;
const int LINE_SIZE = 1024;
	
int getLines(char** lineArray){
	char ch = ' ';
	int lineIndex = 0;
	int stringIndex = 0;
	ch = getchar();
	lineArray[lineIndex] = malloc(LINE_SIZE * sizeof(char));
	while (ch != EOF) {
		if (ch != '\n') {
			lineArray[lineIndex][stringIndex++] = ch;
		} else {
			lineArray[lineIndex][stringIndex] = '\0';
			lineIndex++;
			stringIndex = 0;
			ch = getchar();
			if (ch != EOF && lineIndex != MAX_LINES) {
				lineArray[lineIndex] = malloc(LINE_SIZE * sizeof(char));
				lineArray[lineIndex][stringIndex++] = ch;
			} else {
				if (ch == EOF) {
					puts("End of file!\n");
				} else {
					puts("Maximum line achieved!\n");
				}
				break;
			}
		}
		ch = getchar();
	}
	return lineIndex;
}

long mystrtol(char * start, char ** rest) {
	long result = 0;
	int numberIndexEnd = 0;
	
	while(start[numberIndexEnd] != '\0' && isspace(start[numberIndexEnd])){
		numberIndexEnd++;
	}
	
	if (start[numberIndexEnd] != '\0') {
		char ch = start[numberIndexEnd];
		//putchar(ch);
		int signFlag = 0; // 0 for positive, 1 for negtive
		if (ch == '-') {
			signFlag = 1;
			ch = start[++numberIndexEnd];
		} else if (isdigit(ch)){
			result = result * 10 + (ch - '0');
			ch = start[++numberIndexEnd];
		}
		while (isdigit(ch)) {
			//putchar(ch);
			//printf("value is %ld\n", result);
			result = result * 10 + (ch - '0');
			ch = start[++numberIndexEnd];
		}
		if(signFlag == 1){
			result *= -1;
		}
		*rest = &start[numberIndexEnd];
		return result;
	} else {
		*rest = start;
		return 0;
	}
	
	
}


void sortLines(char **lineArray, int sortFlag, int lineIndex) {
	// 0 normal, 1 fold, 2 numeric, 3 reverse
	long *num;
	if (sortFlag==2){
		num = malloc(lineIndex * sizeof(long));
		char * strTemp;
		for (int k = 0; k < lineIndex; k++){
			num[k] = mystrtol(lineArray[k], &strTemp);
		}
		quicksortN(num,lineArray,0,lineIndex-1);
	}
	else{
		quicksortS(lineArray,0, lineIndex-1, sortFlag);

	}
}



int main(int argc, char *argv[]){
	int reverse=0;
	int sortFlag = 0; // 0 normal, 1 fold, 2 numeric, 3 reverse
	//get command line
	int count=argc-1;
	while(count>0){
		if(strcmp(argv[count], "-h") == 0 || strcmp(argv[count], "-?") == 0) {
			puts("sort strings with different flags!\n");
			return 1;
		} 
		else if (strcmp(argv[count], "-f") == 0) {
			sortFlag = 1;
			puts("fold sorting!\n");
		}
		else if (strcmp(argv[count], "-r") == 0) {
			reverse = 1;
			puts("reverse sorting!\n");
		} 
		else if (strcmp(argv[count], "-n") == 0) {
			sortFlag = 2;
			puts("numeric sorting!\n");
		} else {
			puts("invalid flag!!\n");
			return -1;
		}
		count--;
	} 
		
	// malloc the memory for the array
	char ** lineArray = malloc(MAX_LINES * sizeof(char *));
	
	// get lines
	int lineIndex = getLines(lineArray);
	
	
	// lines got from input
	puts("Got the following lines: \n");
	for (int i = 0; i < lineIndex; i++) {
		puts(lineArray[i]);
	}
	
	
	// check mystrtol
	char line[] = " -56  Cards in a negative deck";
	long value;
	char *rest;
	
	value = mystrtol(line, &rest);
	assert(value == -56);
	assert(rest == &line[4]);
	
	// sort the lines
	sortLines(lineArray, sortFlag,lineIndex);
	
	// lines got from sorting
	puts("Got the following lines after sorting: \n");
	if (reverse){
		for (int i = lineIndex-1; i >-1; i--) { 
			printf("%s\n",lineArray[i]);  
		}
	}		
	else{
		for (int i = 0; i < lineIndex; i++) {
			printf("%s\n",lineArray[i]);
		}
	}
	
	
	// clean up
	for (int i = 0; i < lineIndex; i++) {
		free(lineArray[i]);
	}
	free(lineArray);
	return 0;	
}
