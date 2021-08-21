// Lab project by Sarang Dev Saha (20UCS173)
//LAB6_QUES 1
// Printing the Fibonacci Series.
#include <stdio.h>

int main() {
   // n=number of terms,i= a general term
   int n,i,first_term,second_term,next_term;
   printf("Enter the number of terms in the Fibonacci series: ");
   scanf("%d",&n);
   // Writing the initiation values of the series (remember when n=1, first_term=next_term=0)
   first_term=0;
   second_term=1;
   next_term=0;
   printf("The series is: ");
   // using the for loop with the format for(initiating value, limiting value, increament)
   for(i=1;i<=n;i++){
	   
       printf("%d, ",next_term);
	   // to continue the loop we need to copy the values of a term to the next one.
       first_term=second_term;
       second_term=next_term;
       next_term=first_term+second_term;
   }
   
    
    return 0;
}