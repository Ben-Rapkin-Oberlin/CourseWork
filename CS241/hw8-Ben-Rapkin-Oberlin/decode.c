#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include "workHorse.h"
#include <inttypes.h>
//#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "ahh.h"

// TODO: 


int llvl=0;
int rlvl=0;

typedef struct tree tree;
void freeAll(tree * a);

//function copied from https://www.programiz.com/c-programming/examples/binary-decimal-convert
int convert(long int n) {
  int dec = 0, i = 0, rem;

  while (n!=0) {
    rem = n % 10;
    n /= 10;
    dec += rem * pow(2, i);
    ++i;
  }

  return dec;
}

tree * makeTree(FILE *fpoint, tree* placeHolder){
    // open file
    // construct tree via preorder traversal (root, left, right)
    // following a 1 will be the leaf's value, this will always be
    // a string of 8 1s and 0s

    // I am still unclear on the final formate of an encoded
    // file, right now I am going to assume the tree is on line 0,
    // and the char list is on line 2


    //int pre[] = { 10, 5, 1, 7, 40, 50 };
    //need to convert 
    int* a = malloc(50 * sizeof(int));
    for (int i=0; i<50; i++)
    {
        a[i]=-1;
    }
    int index=0;
    int c = fgetc(fpoint);
    int endFound=0; //EOF
    int leaf=0; //if last value was node then 0, if leaf then one
    int end=0;
    int call=0;
    int sa;
    while (end!=1)
    {
  
    // 0 1 01100101 0 0 1 01110011 1 01101000 0 1 11111111 0 1 01100011 1 00001010
    // to {NULL, e, NULL, NULL, s, h, NULL, EOF, NULL, c, \n}
    // (not actual chars, we want their deciaml values)
        if (c=='0')
        {
           a[index]=-2;
           leaf=0;
        }
        else if (c=='1')
        {
            int count=0;
            char b[9];
            int min=8;
                if (sa<9){
                    min=sa;
                }
            for (int i =0; i<8; i++)
            {
                b[i]=((char) fgetc(fpoint));
                if (call&&leaf){
                    if (a[i]!=b[i]){
                        end=-1; 
                    }
                    count++;
                }
                if (end!=-1 && count==min){
                    end=1;
                    break;
                }
                else{
                    end=0;
                }
            }
            if (end==1){
                break;
            }
            b[8]='\0';
            char *ptr;
            long int temp;
            temp=strtol(b, &ptr, 2);
            leaf=1;
            a[index]=temp;
            if (temp==255){
                endFound=1;
                //need to implement knowlege of where end is as it's place in the 
                //tree denotes the change from tree to parseing 
            }
        }
        index++;
        if (endFound && leaf &&!call){
            char* a=getb();
            int sa=sizeof(a)/sizeof(a[0]);
            call=1;
        }    
         c = fgetc(fpoint);  

        //printf("index: %i",index);
    }

    int count=0;
    while (a[count]!=-1){
        count++;
    } 
    extern int size;
    size=count;
	int fin[count];
    for (int i=0; i<count; i++){
        fin[i]=a[i];
    }

    //I am unsure if i must free all elements in this array
    

    /*   
    for (int i=0; i<11; i++)
    {
        if (isalpha(a[i]))
            printf("%c\n", (char) a[i]); 
        else{
            printf("%i\n", a[i]);
        }
      
    }
    */
    placeHolder=newNode(fin[0]);
    extern tree * original;
    original=placeHolder;
    placeHolder=buildTree(placeHolder,fin);
    //free(original);
    //lvl(placeHolder);
    free(a);
    return placeHolder;

}

void navigateTree(FILE *fpoint, tree* root, tree* current){

    
    while ((char) current->data!=EOF){
        current=root;
        while(current->data==-2){
            char c=(char) fgetc(fpoint);
            //printf("%c\n", c);

            
            if (c=='0'){
                current=current->left;
                //printf("left\n");
            }
            //right
            else if (c=='1'){
                current=current->right;
                //printf("right\n");
            }
            else{
                printf("\nerror, number is not 0 or 1: '%c' \n", c);
                
                exit(-1);
            }
        }
        putchar((char) current->data);
    }

    freeAll(root);
   // free(current);
    putchar(EOF);
}


// file will look like 1010101010
// each 0 means go to a left child
// each 1 means go to right child
// if we hit a leaf, (no children), it will have a char
// print that char
// reset position to top of the tree
// look at next 1/0

void freeAll(tree * a)
{
    if (a->left){
       freeAll(a->left);
       llvl++;
    }
    if (a->right){
        freeAll(a->right);
    	rlvl++;
    }
    free(a);
    return;
}
int main(int argc, char *argv[]){
    //expect argc to be 1
   // printf("argv: %i\n", argv[0]);
    if (argc!=2)
    {
        printf("\nError: Expects 1 argument\n");
        return -1;
    }
    //TODO: deal with errors here

    //call the test method from ahh on outbut.bin
    //have that method over write outbut.bin
    //read from outbut.bin
    convertBin("outbut.bin");
    FILE *fpoint;
    //convertBin will send to temp.txt
    fpoint=fopen("temp.txt","r");
    //creating a tree in static goes badly,
    //so we will just edit it there
    //tree* start = (tree*)calloc(1, sizeof(tree));
    tree* start=makeTree(fpoint,start);
    tree* temp=newNode(-2);
    //pre_order_traversal(start);
    //lvl(start);
    navigateTree(fpoint,start,temp);
    free (temp);
    fclose(fpoint);
    // so far all code up to this point is working, now just have to
    // test w/ valgrind
}






