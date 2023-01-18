#include <stdio.h>


int getdigit() {
	int current=getchar();
	while (current!=EOF){
		switch (current){
			case 48: return (0);
			case 49: return (1);
			case 50: return (2);
			case 51: return (3);
			case 52: return (4);
			case 53: return (5);
			case 54: return (6);
			case 55: return (7);
			case 56: return (8);
			case 57: return (9);
			case 45:
				 current=getchar();
				  switch (current){
					case 48: return (0); 
					case 49: return (-1);
					case 50: return (-2); 
					case 51: return (-3);
					case 52: return (-4);
					case 53: return (-5);
					case 54: return (-6);
					case 55: return (-7);
					case 56: return (-8); 
					case 57: return (-9);   
					
		
				}
		}
		current=getchar();
	}
	return (-1);
}


int main()
{
	int input= getdigit();
	printf("%i\n",input);
	if (input>=0){	
		for (int row=0; row<input;row++){
			char s[row*2+2];
			for (int space=0; space<(input-row); space++){
				printf("%c",' ');
			}
			for (int col=0; col<(row*2+1);col++){
				s[col]='*';
			}
			s[row*2+1]='\0';
			printf("%s\n",s);
		}		 	
		for (int row=input-1; row>0; row--){
			for (int white=0; white<(input-row+1); white++){
				printf("%c", ' ');
			}
			char s[row*2];
			for (int col=0; col<(row*2-1); col++){
				s[col]='*';
			}
			s[row*2-1]='\0'; 
			printf("%s\n",s);	
		}	
	}
	else{
	//	printf("%s","else");
		input=-input;
		for (int row=0; row<input;row++){      
			char s[row*2+2];
			for (int space=0; space<(input-row); space++){
				printf("%c",'*');
			//	printf("%s","space");
			}
			for (int col=0; col<(row*2+1);col++){
				s[col]=' ';
			}
			s[row*2+1]='\0';
			printf("%s",s);
			/*char w[input-row];
			for (int outside=0; outside<input-1-row; outside++){
				w[outside]='*';		
			}
			w[input-row]='\0';
			printf("%s", w);
			*/
			for (int space=0; space<(input-row); space++){                                                                                                                                                                             printf("%c",'*');    
			}
			printf("\n");
		}

		for (int row=input-1; row>0; row--){ 
			for (int white=0; white<(input-row+1); white++){
				printf("%c", '*');
			}
			char s[row*2];
			for (int col=0; col<(row*2-1); col++){
				s[col]=' ';
			}
			s[row*2-1]='\0';
			printf("%s",s); 
			for (int white=0; white<(input-row+1); white++){
				printf("%c", '*');
			}     
		      printf("\n");	



		}
	}
}
