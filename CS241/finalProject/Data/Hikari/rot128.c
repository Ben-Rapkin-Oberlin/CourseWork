/*
Made by Hikari
Takes each character from input and outputs it rotated by half its allowed value. 
*/
#include <stdio.h>
#include <limits.h>
char x;
int done, add;

int main(){
	add = (UCHAR_MAX + 1)/2;
	done = 0;
	while(!done){
		x = (char)getchar();
		if(x != -1){
			x = x + add;
			putchar((int)x);
		}
		else{
			done = 1;
		}}}

