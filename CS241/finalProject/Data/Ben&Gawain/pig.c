//ben rapkin and gawain liu
#include<stdio.h>
#include<string.h> 
#include <ctype.h> 


int leadingVowel(char *word, int count){
    //check for capitalization
    //aeiou. 
    //!qu, it's a con
    //!y for leading, but y for shift
    if (word[0]==65||word[0]==69||word[0]==73||word[0]==79||word[0]==85 ||word[0]== 97||word[0]==101||word[0]==105||word[0]==111||word[0]==117){           
    //add yay                
        word[count]=121;
        word[count+1]=97;
        word[count+2]=121;
        word[count+3]='\0';
        return 1;
    }
    return 0;
}

void leadingCon(char *word, int count){
    //shift until vowel to end
    int vowel=0;
    int index=-1;
    char temp [110];
    int upper=0;
    if (isupper(word[0])){
	//preserves case
	upper=1;
	word[0]=tolower(word[0]);
    }
    while (!vowel && index<count-1){
        index++;
    	if (word[index]==65||word[index]==69||word[index]==73||word[index]==79||word[index]==85 ||word[index]== 97||word[index]==101||word[index]==105||word[index]==111||word[index]==117){
		if(!((word[index]==117||(word[index]==85)) && (word[index-1]==113 ||word[index-1]==81))){
			//if the current letter is a not a u with a q before it, then cont. 
			//otherwise, pretend no vowels found
			vowel=1;
	}
        }
    }
    strcpy(temp,word);
    if (vowel){	
    	for (int i=0; i<(count-index); i++){
        	word[i]=temp[i+index];
    	}	
    	for (int i=0; i<index; i++){
        	word[i+count-index]=temp[i];
    	}
    }
    if (upper){
	word[0]=toupper(word[0]);
    }	
    word[count]=97;
    word[count+1]=121;
    word[count+2]='\0';
}

void reset(char *word){
    for (int i=0; i<110; i++){
        word[i]='\0';
    }
}

int main(int argc, char **flags){
   if(argc>1&&strncmp(flags[1],"-",1)==0){
	if(strncmp(flags[1],"-h",2)==0||strncmp(flags[1],"-?",2)==0){       	  
	   printf( "\npig.c will take in text and convert it to pig latin while\npreserving puctuation and capitalization. Once complete it\nwill return 0! This message will return 1 and an\nunknown flag will return -1!\n\n");
	   		return 1;
		   }
		   else{
			printf("flag not known, please try -h or -?\n");
			return -1;
	}
    }
    char word [110];
    int current=0;
    int count=0;
    while (current!=EOF){
    	//scans words and punc
   	current=getchar();
        while ((current>=65 && current<=90) | (current>=97 && current<=122)) {
        // this is the word thingy, checks that char is upper or lower
            word[count]=current;
            current=getchar();
            count++;
        }
        word[count]='\0';
        if (word[0]!='\0'){
            if (!leadingVowel(word,count)){
                leadingCon(word,count);
            }
            printf("%s",word);
        }
	count=0;
	if (current!=EOF){
		//I'm doing it here instead of the top becuase the first time current is artificially 0
		//and I don't want to risk a null bit screwing with the output
		putchar(current);
	}
    }
    return 0;
}
