// Lab project by Sarang Dev Saha (20UCS173)
//LAB6_QUES 
/* Write a program to print a half pyramid pattern. */
#include <stdio.h>
int main() {
   int i, j, rows;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = 1; i <= rows; ++i) {
      for (j = 1; j <= i; ++j) {
         printf("%d ", j);
      }
      printf("\n");
   }
   return 0;
}
