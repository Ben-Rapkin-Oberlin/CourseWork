//Ben Rapkin and Gawain Liu
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 255
#define MAX_COINS 100
#define MAX_CHANGE 100

#define DEBUG 0 // Change DEBUG to 1 to print extra information

/* calculate_change
   inputs:
   	int change - How much change we are making
        int num_coins - How many coins are in the coins array
        int coins[] - The coins used for change
        int coins_returned[] - Array where we will store how many coins are returned per change
        int next_coin[] - Array where we will store the next change step.
   returns:
        int how many coins are required for change units
   Algorithm:
        Check if we have solved the change problem for this number.  If so, just return.
        If we have not solved it, iterate through the coins, and pick the best one.
        Store those values in our arrays so we do not repeat the work
*/

int calculate_change(int change, int num_coins, int coins[], int coins_returned[], int next_coin[]) {

  int min_change = MAX_CHANGE; // Set it to the maximum possible value
  int change_found = 0;

  // Check if we have found a solution for this change already
  if (coins_returned[change] != -1) {
    if (DEBUG) {
      printf("Found prior result of %d at %d\n", coins_returned[change], change);
    }
    return(coins_returned[change]);
  }
  
  // Calculate the change for the each coin
  for (int i = 0; i < num_coins; i++) {
    // Make sure we can use this coin
    if (change - coins[i] >= 0) {
      // Recurse using this coin to make change.
      change_found = 1 + calculate_change(change - coins[i], num_coins, coins, coins_returned, next_coin);
      if (change_found < min_change) {
        // TODO: Update min change
        min_change = change_found;

        // TODO: Update coins_returned array
        coins_returned[change] = min_change;

        // TODO: Update next_coin array to where we go next for change
        next_coin[change] = change - coins[i];

      }
    }
  }
  
  return min_change;
}




int main() {
  
  char *rv = NULL;
  char buf[MAX_LENGTH];

  int change = 0;
  int num_coins = 0;
  char *rest = NULL;
  char *tok = NULL;
  int read = 0;
  int *coins = NULL;

  int coins_returned[MAX_COINS];
  int next_coin[MAX_COINS];
  int change_count = 0;
  
  // Read a line of input: change num_coins coin_1 coin_2 coin_3 ...
  while ((rv = fgets(buf, MAX_LENGTH, stdin)) != NULL) {
    read = sscanf(buf, "%d %d %m[0-9 ]", &change, &num_coins, &rest);
    
    coins = (int*)malloc(sizeof(int) * num_coins);
    if (coins == NULL) {
      fprintf(stderr, "Could not allocate memory for coins array.\n");
      free(rest);
      exit(1);
    }
    // Extract rest into coins[];
    int i = 0;
    if ( (tok = strtok(rest, " ")) != NULL) {
      coins[i++] = atoi(tok);
    }
    while ( (tok = strtok(NULL, " ")) != NULL) {
      // Do some error handling just in case
      if (i == num_coins) {
        fprintf(stderr, "Line contained more coins than were specified.");
        free(coins);
        free(rest);
        exit(1);
      }
      coins[i++] = atoi(tok);
    }

    printf("Using coins ");
    for (i = 0; i < num_coins; i++) {
      printf("%d ", coins[i]);
    }
    // We will no longer need rest at this stage of the while loop, so free it.
    free(rest);

    coins_returned[0] = 0;
    next_coin[0] = 0;
    // TODO: Initialize coins_returned and next_coin arrays.
    // Don't forget what to do with known coins!
    for (int i = 1; i < MAX_COINS; i++) {
    	coins_returned[i] = -1;
    	for (int j = 0; j < num_coins; j++) {
	    // Make sure we can use this coin
	    if (i - coins[j] >= 0) {
	    	next_coin[i] = i - coins[j];
		break;
	    }
	}
    }

    change_count = calculate_change(change, num_coins, coins, coins_returned, next_coin);
    printf(", change for %d required %d coins: ", change, change_count);

    i = change;
    int next = 0;

    next = change;
    for (i = 0; i < change_count; i++) {	
	    printf("%d ", next - next_coin[next]);
	    next = next_coin[next];
    }
      
    printf("\n");
    free(coins);
     
     
     if (DEBUG == 1) {
	i = 1;
     

	while (coins_returned[i] != -1) {
		printf("%d: %d, %d\n", i, coins_returned[i], next_coin[i]);
		i++;
	   }
 	}
      }

   // We have reached the end of the file.
   exit(0);
 
}	
