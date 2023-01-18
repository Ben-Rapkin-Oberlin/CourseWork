/* Code by Hikari Mertensotto and Zorah Salke. 4/20/2022. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <ctype.h>

void help();

/* Checks a character against all lowercase vowel values. */
int isVowel(int c){
	int vowels[6] = {97, 101, 105, 111, 117, 121};
	for (int i = 0; i <= 6; i++){
		if (c == vowels[i]){
			return 1;
		}
	}
	return 0;
}
//takes in a string to translate and an integer that determines which translation to use, 0 for Pig Latin and 1 for 1337. Then returns the string with the translation applied.
char * translate(char *word , int opt){
	/* If the user has selected Pig Latin. */
	if(opt == 0){
		int first = word[0];
		int cap = 0; //tracks captialization
		int vs = 0; //tracks if it starts with a vowel
		if(first > 64 && first < 91){
			cap = 1;
			first = first + 32; //this converts the char to lowercase
			word[0] = first; 
		}
		if(isVowel(first)){ //checks if starts with vowel 
			vs = 1;
		}
		if(vs == 1){ //adds yay if it starts with a vowel
			if(cap == 1){ //recapitalizes
                		word[0] = word[0] - 32; 
			}
			strcat(word, "yay");
		       	return word;
		}
		else{
			char temp[102] = {0}; //should never go past this size given the input range
			char temp2[102] = {0};
			int done = 0;
			int count = 1;
			while(done == 0){ //loops until count = the position of first vowel, and first = first vowel	
				first = word[count]; // here, first is used to find the first vowel
				
				if(first > 64 && first < 91){
					first += 32;
				}
				if(first == 0){//if it reaches the end of the word without finding a vowel it just returns it
					return word;
				}
				if(isVowel(first)){ //checks for vowels
					if ( !(first == 117 && (int)word[count-1] == 113) ) { //does nothing if qu
						done = 1;
					}
				}
				if(done != 1){
					++ count; 
				}
			}
			int i;
			for(i = 0; i < count; ++ i){ //copies up to vowel to temp, adds ay
				temp[i] = word[i];
			}
			strcat(temp, "ay");
			done = 0;
			i = 0;
			while(done == 0){ //copies everything from first vowel after to temp2
				if((int)word[count + i] == 0){
					done = 1;
				}
				else{
					temp2[i] = word[count + i];
					++ i;
				}
			}
			strcat(temp2, temp); //combines temp2 and temp to create translated word
			if(cap == 1 && temp2[0] > 96 && temp2[0] < 123){
				temp2[0] = temp2[0] - 32; //converts back to capital
			}
			strcpy(word, temp2);
			return word;
		}
	}
	/* If the user has selected 1337. */
	else if(opt == 1){
		char cur = 0;
		char temp[400] = {0}; //should never go past this size given the input range
		int done = 0;
		int count = 0;
		while(done == 0){ //loops until the entire word has been translated, adding the 1337 translation to temp as it goes and then returning the translated word
			cur = word[count];
			if(cur > 64 && cur < 91){
                        	cur += 32; //this converts the char to lowercase for standardization purposes
			}
			if(cur == 0){ //returns word when done
				int length = strlen(temp);
				
				if (temp[length-1] == 82){//temp[length] = \0 due to array indexing beginning from 0.
					if (temp[length-2] == 51){
						//checks if word ends in "3R". now uppercase due to check for isalpha() at bottom
						//butler -> BU7LXX0R
						temp[length-2] = 'X';
						temp[length-1] = 'X';
						temp[length] = 48;
						temp[length+1] = 'R';
						length += 1; 
					}	
				}
				
				temp[length+1] = '\0';
				strcpy(word, temp);
				return word;
			}
			if(cur == 97){ //checks to see which letter cur is based on the ascii value, then adds the 1337 equivelant to temp
					strcat(temp, "4");
			}
			else if(cur == 99){
					strcat(temp, "<");
			}
			else if(cur == 101){
					strcat(temp, "3");
			}
			else if(cur == 103){
					strcat(temp, "6");
			}
			else if(cur == 104){
					strcat(temp, "|-|");
			}
			else if((cur == 105)||(cur == 108)){
					strcat(temp, "1");
			}
			else if(cur == 109){
					strcat(temp, "/\\/\\");
			}
			else if(cur == 110){
					strcat(temp, "|\\|");
			}
			else if(cur == 111){
					strcat(temp, "0");
			}
			else if(cur == 115){
					strcat(temp, "5");
			}
			else if(cur == 116){
					strcat(temp, "7");
			}
			else if(cur == 118){
					strcat(temp, "\\/");
			}
			else if(cur == 119){
					strcat(temp, "\\v/");
			}
			else if(cur == 122){
					strcat(temp, "2");
			}
			else {
				if (cur < 123 && cur > 96){
					cur = cur - 32; //converts to uppercase for typeface consistency
				}
				strncat(temp, &cur, 1); //copies character if it isn't one of the listed alphabet
			}
			count++;
		}
	}
	
	return "-1"; 
	//ensures the function has a return statement in general
	//will be handled as an error because the function should meet one of the conditions above

}
