//Made By Hikari
//This program loops through standard input until it reaches an EOF singal, keeping track of each character and storing it's count in an array. It then prints the frequencies, and the most and least occuring characters.

#include <stdio.h>

int count[256];
int cur_char, cur_count, total, i, min, max;
float percent;
char cur;

int main(){
	for(i = 0; i < 256; ++ i){
		count[i] = 0;
	}
	cur_char = getchar();
	while(cur_char != -1){
		if(cur_char > 32){
			++ count[cur_char];
			++ total;
		}
		cur_char = getchar();
	}
	printf("%s\n", "char	Frequencies	Percentage");
	min = 2147483647;
	max = 0;
	for(i=33; i < 256; ++ i){
		cur_count = count[i];
		if(cur_count > 0){
			if(cur_count < min){
				min = cur_count;
			}
			if(cur_count > max){
				max = cur_count;
			}
			cur = (char) i;
			percent = (float)cur_count / (float) total * (float) 100;
			printf("%c%s%d%s%f\n", cur, ":	", cur_count, "		", percent);
		}
	}
	printf("%s", "Maximum Character(s): ");
	for(i=33; i < 256; ++ i){
		if(count[i] == max){
			cur = (char) i;
			printf("%c%s", cur, " ");
		}
	}
	printf("\n");
	printf("%s", "Minumum Character(s): ");
	for(i=33; i < 256; ++ i){
		if(count[i] == min){
			cur = (char) i;
			printf("%c%s", cur, " ");
		}
	}
}
