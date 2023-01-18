
#include <time.h>
#include <stdio.h>
clock_t start, end;

int loop(int n){
    int sum=0;
    for (int i=0; i<n; i++){
        sum++;
    }
    return sum;

}


int main(){
    int n=100000000;
    clock_t t;
    t = clock();
    printf("%i\n",loop(n));
    t = clock() - t;
    //double time_taken = ((double)t)/CLOCKS_PER_SEC; // calculate the elapsed time
    //printf("%f seconds", time_taken);
    printf("%f seconds", t);

}