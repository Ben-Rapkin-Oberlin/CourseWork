//Made By Hikari, 4/23/2022
//Description:
// Reads in from standard input line by line, storing the lines in a char** array.
// Then sorts the lines as specified by flags (full flags and sorting options can be seen by running ./sort -h or ./sort -?), using qsort and comparing lines with strcmp (in a custom function that translates from pointers to strings) by default. Then prints the sorted lines.
#include <stdio.h>
#include <string.h>
#include <strings.h> 
#include <stdlib.h>

long mystrtol(char *start, char **rest);
void mymergesort(char** array, int left, int right, int (*comp)(const void*, const void*));
int linestrcomp(const void **line1, const void **line2);
int linestrfcomp(const void **line1, const void **line2);
int linenumcomp(const void **line1, const void **line2);
int linenumfcomp(const void **line1, const void **line2);
void help();

int main(int argc, char* argv[]) {
	int opt = 0; //default
	int rev = 0; //tracks rev
	int myqs = 0; //tracks if using myqsort
	int fold = 0; // tracks folding option
	int i;
	for (i=1; i<argc; i++) { //if there are aditional flags, reads them in and changes opt
		if (strcmp(argv[i], "-h") == 0){
			help();
			exit(-1);
		} else if (strcmp(argv[i], "-?") == 0) {
			help();
			exit(-1);
		} else if (strcmp(argv[i], "-n") == 0) {
			opt = 1;
		} else if (strcmp(argv[i], "-f") == 0) {
			fold = 1;
		} else if (strcmp(argv[i], "-r") == 0) {
			rev = 1;
		} else if (strcmp(argv[i], "-m") == 0) {
			myqs = 1;
		} else {
			printf("%s\n", "You have entered an invalid flag.");
			help();
			exit(-1);
		}
	}
	char **larray; //stores lines as pointers to character pointers to start of each line
	larray =  malloc(1048576 * sizeof(char *));
	int lcount = 0; //stores line count
	int llen = 0; //stores lenght of line
	char *line; //stores lines temporarily
	int c; //stores current character read in
	line = malloc(1024*sizeof(char *)); //assuming byte char, should be 1024 bytes of data
	while ((c = getchar()) != EOF){
		if(llen == 1023){
			line[1023] = '\0';
		}
		else if(c == 10){ //when at \n, increase line
			line[llen] = '\0';
			larray[lcount] = line; //stores current line address in array
			++ lcount;
			if(lcount == 1048575){ //program gives error and exits if more than 1,048,576 lines are passed to it
				printf("%s\n", "This program can only handle 1,048,576 lines of input. Please try again with a smaller input.");
				exit(-1);
			}
			llen = 0; //resets llen 
			line = malloc(1024 * sizeof(char)); //alocates new memory for next line	
		}
		else if(llen < 1023){ //only stores line if space, characters get dumped if too long
			line[llen] = c;
			++ llen;
		}
	}
	free(line); //frees the line that is created when \n is found at the end of the file
	if(opt == 0){ //sorts normally
		if(myqs == 0){ //normal qs
			if(fold == 1){ //folding sort if flagged
				qsort(larray, lcount, sizeof(char *),(int(*)(const void*,const void*)) linestrfcomp);
			}
			else{ //normal sort
				qsort(larray, lcount, sizeof(char *),(int(*)(const void*,const void*)) linestrcomp);
			}
		}
		else{
			if(fold == 1){ //folding sort if flagged
				mymergesort(larray, 0, lcount - 1, (int(*)(const void*,const void*)) linestrfcomp);
			}
			else{ //normal sort
				mymergesort(larray, 0, lcount - 1, (int(*)(const void*,const void*)) linestrcomp);
			}
		}
	}
	else if(opt == 1){ //sorts by leading number
		if(myqs == 0){ //normal qs
			if(fold == 1){ //folding sort if flagged
				qsort(larray, lcount, sizeof(char *),(int(*)(const void*,const void*)) linenumfcomp);
			}
			else{ //normal sort
				qsort(larray, lcount, sizeof(char *),(int(*)(const void*,const void*)) linenumcomp);
			}
		}
		else{
			if(fold == 1){ //folding sort if flagged
				mymergesort(larray, 0, lcount - 1,(int(*)(const void*,const void*)) linenumfcomp);
			}
			else{ //normal sort
				mymergesort(larray,0,  lcount - 1,(int(*)(const void*,const void*)) linenumcomp);
			}
		}
	}

	printf("%s\n", "Sorted Lines:");
	if(rev == 0){ //prints sorted lines
		for(i = 0; i < lcount; i++){
				line = larray[i];
				printf("%s\n", line);
		}
	}
	else{ //prints reverse order sorted lines
		for(i = lcount - 1; i > -1 ; i--){
				line = larray[i];
				printf("%s\n", line);
		}
	}

	//frees allocated memory
	for(i = 0; i < lcount; i++){
		free(larray[i]);
	}
	free(larray);
}

void help(){ //prints help
	printf("%s\n%s\n%s\n%s\n%s\n%s\n", "This program sorts a file by line according to strcmp. The program reads from standard input, to use it redirect a file or type in text typing EOF on a new line (likely Ctr+D) when done", "Flags:", "To access this help page, use -? or -h.", "To reverse the order of the output of the search, use -r", "To sort lines by leading number, use -n", "To sort with my implementation of mergesort, use -m");
	return;
}

long mystrtol(char *start, char **rest){ //takes a pointer to the start of a string, skips leading whitespace, and converts the next characters that are numbers into a long int. Then, stores the address of the first character after the number in rest and returns the long int
	int cur; //stores current character
	int pos = 0; //stores position in string
	long value = 0;
	while((cur= start[pos]) == 9 || cur == 32){ //increments pos to after tabs or spaces
		++ pos;
	}
	int neg = 0; //tracks if negative
	if(cur  == 45){//if -
		++ pos;
		cur = start[pos];
	}
	if(cur > 47 && cur < 58){ //checks if leading number
		value = value + cur - 48; //converts cur to num, adds to value
	}
	else{ //sets start and returns 0 if no number
		*rest = start;
		return 0;
	} 
	++ pos;
	cur = start[pos];
	while(cur > 47 && cur < 58){//loops, adding numbers to value until at end of numbers
		value = value << 1;
		value = value + cur - 48;
		++ pos;
		cur = start[pos];
	}
	*rest = &start[pos];
	if(neg == 1){
		value = value * -1;
	}
	return value;
}

int linestrcomp(const void **line1, const void **line2){ //comparison function that dereferences the lines and returns the result of the line strings being passed to strcmp
	char *s1 = *(char **)line1;
	char *s2 = * (char **) line2;
	return strcmp(s1, s2);
}

int linestrfcomp(const void **line1, const void **line2){ //same as above function but with strcasecmp
	char *s1 = * (char **) line1;
	char *s2 = * (char **) line2;
	return strcasecmp(s1, s2);
}

//compator for numeric sorting. Takes two strings, runs mystrtol on them, then sorts by leading number. If these are the same, the rest of the string norrmally. Returns -1 if first sring should come before, 0 if they are the same, and 1 if the second string should come first.
int linenumcomp(const void **line1, const void **line2){ 
	char *s1 = *(char **)line1;
	char *s2 = *(char **)line2;
	long n1, n2;
	char *rest1;
	char *rest2;
	n1 = mystrtol(s1, &rest1);
	n2 = mystrtol(s2, &rest2);
	if(n1 < n2){
		return -1;
	}
	else if(n1 > n2){
		return 1;
	}
	else{
		return strcmp(rest1, rest2);
	}
}
//same as above function, but sorts by strcasecmp instead if the leading numbers are the same
int linenumfcomp(const void **line1, const void **line2){ 
	char *s1 = * (char **) line1;
	char *s2 = * (char **) line2;
	long n1, n2;
	char *rest1;
	char *rest2;
	n1 = mystrtol(s1, &rest1);
	n2 = mystrtol(s2, &rest2);
	if(n1 < n2){
		return -1;
	}
	else if(n1 > n2){
		return 1;
	}
	else{
		return strcasecmp(rest1, rest2);
	}
}

//runs mergesort on an array of **. left is the leftmost index (start of array) and right is the rightmost index (last element in array)
void mymergesort(char** array, int left, int right, int (*comp)(const void*, const void*)){
	if(left == right){ //base case for single element
		return;
	}
	int mid = left + ((right - left) / 2);
	mymergesort(array, left, mid, comp); //mergesorts first half
	mymergesort(array, mid + 1, right, comp); //mergesorts second half
	//merges the two halves
	int sort;
	int lefti = left; //tracks index of left array when merging
	int righti = mid + 1; //tracks index of right array when merging
	int ti = left; //tracks index of temp array
	char **tarray =  malloc(1048576 * sizeof(char *)); //temporary array for swap, size of max array size
	while(lefti < mid + 1 && righti < right + 1){ 
		sort = (*comp)((void *)&array[lefti], (void *) &array[righti]); //0 if equal,  <0 if first should come before, >0 if first should come after
		if(sort < 1){ //puts left array element first if it needs to, or if equal
			tarray[ti] = array[lefti];
			++ ti;
			++ lefti;
			tarray[ti] = array[righti];
			++ti;
			++righti;
		}
		else{ //puts right array element first
			tarray[ti] = array[righti];
			++ti;
			++righti;
			tarray[ti] = array[lefti];
			++ ti;
			++ lefti;
		}
	}
	if(lefti < mid + 1){ //copies extra elements in left (when done, lefti = mid + 1, since it stores mid and then does ++lefti)
		tarray[ti] = array[lefti];
	}
	int i;
	for(i = left; i < right + 1; i++){ //sets elements in array to elements in tarray
		array[i] = tarray[i];
	}
	free(tarray);
}



