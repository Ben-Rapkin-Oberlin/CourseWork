//Ben Rapkin and Gawain Liu
#include<stdio.h>
#include<limits.h>

#define len 300

int array[len]={0};

int max[len]={0};
int min[len]={0};

int minval=1000000;
int maxval=-1000000;

int mintest=0;
int maxtest=0;

int current;

int sum=0;


int main (){
	current=getchar();
	//read all input and increment
	while (current!=EOF){
		array[current]=array[current]+1;
		sum=sum+1;
		current=getchar();
		}

	//listing all the min and max
	for (int i=0; i<len; i++){
		
		//minval and min
		if (array[i]<minval && array[i]!=0){
			for (int j=0; j<len; j++){
				min[j]=0;
			}
			min[i]=1;
			minval=array[i];
		}
		if (array[i]==minval){
			min[i]=1;
		}


		//now maxval and max
		if (array[i]>maxval){  
			for (int j=0; j<len; j++){                      
				max[j]=0;
			}
			max[i]= 1;
			maxval=array[i];
		}            
		if (array[i]==maxval){
			max[i]=1;       
		}
	}

	//now print list
	printf("%s","char        Frequencies         Percentage  (Dec Value)\n");

	for (int i=1; i<len; i++){
		if (array[i]!=0){
			printf("%-1c%-11s%-7i%20f  (%i)\n", i, ":", array[i], (double) array[i]/sum, i);
		}
	}
	//print minmax
	printf("The Least used chars(s) at %i occurances:\n", minval);
	for (int i=0; i<len; i++){
		if (min[i]==1){
			printf("\"%c\" (char %i) ",i,i);
		}
		
	}
	printf("\n");

	printf("The Most used char(s) at %i occurances:\n", maxval);
        for (int i=0; i<len; i++){
		if (max[i]==1){
			printf("\"%c\" (char %i) ",i,i);
                }          

	}
	printf("\n");
	
				



}
