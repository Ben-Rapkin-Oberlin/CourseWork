/*
Made by Hikari
prints a diamond of a given size one through nine, inverted if negative. Looks for first positive or negative interger in the input to determine size. 
*/
#include <stdio.h>
#include <stdlib.h>

int getdigit(), s, d, x, done, neg, inv, size, half, i;

int main(){
	printf("%s", "For the size of the diamond, enter a positive or negative digit from 1-9 (or press crtl+d to quit): ");
	size = getdigit();
	if(size == 10){
		return 0;
	}
	else if(size > 0){
		inv = 0;
	}
	else{
		inv = 1;
		size = abs(size);
	}
	printf("\n");	
	d = 1;
	s = size-1;
	half = 0;
	if(!inv){
		while(d > 0){
			for(i = 0; i < s; ++i){
				printf("%c", ' ');
			}
			for(i = 0; i < d; ++i){
				printf("%c", '*');
			}
			printf("\n");
			if(s == 0){
				half = 1;
			}
			if(!half){
				++d;
				++d;
				--s;
			}
			else{
				--d;
				--d;
				++s;
			}
		}
	}
	else{
		while(d > 0){
			for(i = 0; i < s; ++i){
				printf("%c", '*');
			}
			for(i = 0; i < d; ++i){
				printf("%c", ' ');
			}
			for(i = 0; i < s; ++i){
				printf("%c", '*');
			}
			printf("\n");
			if(s == 0){
				half = 1;
			}
			if(!half){
				++d;
				++d;
				--s;
			}
			else{
				--d;
				--d;
				++s;
			}
		}
	}
}
			





//The function outputs the first positive or negative digit from input, outputs ten when there is no digit in the input
int getdigit(){
	done = 0;
	neg = 0;
	while(!done){
		x = getchar();
		if (x == -1){
			return 10;
		}
		else if(x == 45){
			neg = 1;
		}
		else if(!neg && x < 58 && x > 48){
			if(x == 49){
				return 1;
			}
			else if(x == 50){
				return 2;
			}
			else if(x == 51){
				return 3;
			}
			else if(x == 52){
                        	return 4;
			}
			else if(x == 53){
                        	return 5;
                        }
                        else if(x == 54){
                        	return 6;
                        }
                        else if(x == 55){
                        	return 7;
                        }
			else if(x == 56){
                        	return 8;
                        }
                        else{
                        	return 9;
                        }}
		else if(neg && x < 58 && x > 48){
			if(x == 49){
				return -1;
                        }
                        else if(x == 50){
                        	return - 2;
                        }
                        else if(x == 51){
                        	return -3;
                        }
                        else if(x == 52){
                        	return -4;
                        }
                        else if(x == 53){
                        	return -5;
                        }
                        else if(x == 54){
                        	return -6;
                        }
                        else if(x == 55){
                        	return -7;
                        }
                        else if(x == 56){
                        	return -8;
                        }
                        else{
                        	return -9;
                        }}
		else{
			if(neg){
				neg = 0;
			}
		}
	}
	return 10; //put this line here to appease the compiler and not get an error, the porgram should never reach this point
}

