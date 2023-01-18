#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

struct bigInt {
    int digit;
    struct bigInt* next, * prev;
};

typedef struct bigInt bigInt;

struct bigInt* reader(char n, struct bigInt* a) {
    bigInt* start = (bigInt*)calloc(1, sizeof(bigInt));
    start = a;
    while (n != EOF && n != '\n') {
        \
            //skip leading whitespaces
            while (isspace(n)) {
                n = getchar();
            }
        //read digits
        if (isdigit(n)) {
            a->digit = n - 48;
            n = getchar();
            while (isdigit(n)) {
                bigInt* b = (bigInt*)calloc(1, sizeof(bigInt));
                b->digit = n - 48;
                a->next = b;
                b->prev = a;
                a = b;
                n = getchar();
            }

        } //// need to ignore non digit start ones
        else {
            a->digit = 0;
            a->next = NULL;
            a->prev = NULL;
            while (n != '\n') {
                n = getchar();
            }
            break;
        }
    }
    return start;
}

// changes 12 to 1,2
void redistribute(struct bigInt* end) {
    int c = 0;

    //printf("%i",end->digit);
    //printf("%i",end->prev->digit);
    while (end->prev != NULL) {
        //printf("%i\n",end->digit);
        if ((end->digit) > 9) {
            end->digit = (end->digit) - 10;
            end->prev->digit = (end->prev->digit) + 1;
        }
        c++;
        end = end->prev;
    }
}

struct bigInt* add(struct bigInt* a, struct bigInt* b) {
    int sizeA = 1;
    int sizeB = 1;

    while (a->next) {//while next is not null
        sizeA++;
        a = a->next;
    }
    // printf("finished a\n");
    while (b->next) {//while next is not null
        sizeB++;
        b = b->next;
    }
    // printf("finished b\n");
    if (sizeA<=sizeB){
        while (a->prev){
            a=a->prev;
        }
        while (sizeA<=sizeB){
            bigInt* temp = (bigInt*)calloc(1, sizeof(bigInt));
            a->prev=temp;
            a=a->prev;
            sizeA++;
            free(temp);       
        }
         while (a->next){
            a=a->next;
        }
    }

    for (int i=0; i<sizeB;i++){
        a->digit=a->digit+b->digit;
        a=a->prev;
        b=b->prev;
    }

    while (a->next){
            a=a->next;
    }

    redistribute(a);
    
    flist(b);
    while (a->prev){
            a=a->prev;
    }
    return a;
}

int notZero(struct bigInt* a){
    while (a->prev){
        a=a->prev;
    }
    if (a->digit!=0){
            return 1;
        }
    while (a->next){
        a=a->next;
        if (a->digit!=0){
            return 1;
        }
    }
    return 0;
}

void plist(struct bigInt* sum) {
    //
    int leadO = 0;
    //printf("%i\n",sum->digit);
    //printf("%i\n",sum->next->digit);
    //printtf("notZero: %i",notZero())
    printf("Total: ");
    if (sum->digit != 0 || !(sum->next)) {
        leadO = 1;
        printf("%i\n", sum->digit);
    }
    while (sum->next) {
        sum = sum->next;
        if (sum->digit || leadO) { //if digit is !=0 or if we know its a sigfig
            printf("%i", sum->digit);
            leadO = 1;
        }
    }
    
    if (!notZero(sum)){
        printf(" put 0");
    }
    putchar('\n');
}

struct bigInt* multiply(struct bigInt* a, struct bigInt* b) {
    bigInt* fin = (bigInt*)calloc(1, sizeof(bigInt));
    struct bigInt* curMul = (bigInt*)calloc(1, sizeof(bigInt));
    int sizeA = 1;
    int sizeB = 1;
    int place = 0;

    while (a->next != NULL) {//while next is not null
        sizeA++;
        a = a->next;
    }
    // printf("finished a\n");
    while (b->next != NULL) {//while next is not null
        sizeB++;
        b = b->next;
    }
    // printf("finished b\n");
     //make fin 1 digit longer than the longest num
    for (int i = 0; i < sizeA + sizeB - 1; i++) {
        bigInt* t = (bigInt*)calloc(1, sizeof(bigInt));
        fin->next = t;
        t->prev = fin;
        fin = t;

        bigInt* t_cur = (bigInt*)calloc(1, sizeof(bigInt));
        curMul->next = t_cur;
        t_cur->prev = curMul;
        curMul = t_cur;

        //printf("loop %i",i);
    }


    /*while (fin->prev!=NULL){
        printf("rev: %i \n",fin->digit);
        fin=fin->prev;
        }
        */

        //printf("finished expanding\n");
    struct bigInt* iterA = a;
    //multiply a and b, loop through b, 
    while (place < sizeB) {
        int placeA = 0;
        int carry = 0;

        while (placeA < sizeA) {


            curMul->digit = (iterA->digit * b->digit + carry) % 10;
            //printf("%i, %i", sizeA, placeA);
            carry = (iterA->digit * b->digit + carry) / 10;
            curMul = curMul->prev;
            iterA = iterA->prev;
            placeA++;
        }
        //plist(curMul);
        iterA = a;
        int steps = 0;
        while (curMul->next != NULL) {//while next is not null
            curMul = curMul->next;
            steps++;
        }

        int index = 0;
        while (index < place) {
            bigInt* t_cur = (bigInt*)calloc(1, sizeof(bigInt));
            t_cur->digit = 0;
            curMul->next = t_cur;
            t_cur->prev = curMul;
            curMul = t_cur;
            index++;
        }
        index = 0;
        while (index < steps + place - 1) {//while next is not null
            curMul = curMul->prev;
            index++;
        }

        b = b->prev;
        place++;
        fin = add(fin, curMul);
        while (curMul->next != NULL) {//while next is not null
            curMul = curMul->next;
        }

    }

    // printf("finished copying\n");
     //redistribute(end);
     //printf("finished redist\n");
    free(iterA);
    free(curMul);
    return fin;
}


int main() {
    char n = getchar();
    bigInt* sum = (bigInt*)calloc(1, sizeof(bigInt)); //should initilize all to 0 or NULL

    bigInt* mul = (bigInt*)calloc(1, sizeof(bigInt)); //should initilize all to 0 or NULL
    mul->digit = 1;
    while (n != EOF) {
        bigInt* new1 = (bigInt*)calloc(1, sizeof(bigInt));
        new1 = reader(n, new1);

        //sum = add(sum, new1);
        // order matters for add and multiply, sum and mul must be first
        mul = multiply(mul, new1);
        plist(mul);
        //plist(mul);
        n = getchar();
        free(new1);
    }
    free(sum);
    free(mul);
}