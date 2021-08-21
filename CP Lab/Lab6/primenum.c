// Lab project by Sarang Dev Saha (20UCS173)
//LAB6_QUES 
/* Write a program to print a half pyramid pattern. */
#include <stdio.h>    
     
int main(void)
{
 for (int i=2; i<50; i++)
 {
  for (int j=2; j<=i; j++)   // Changed upper bound
  {
    if (i == j)  // Changed condition and reversed order of if:s
      printf("%d,",i);
    else if (i%j == 0)
      break;
  }
 }
}