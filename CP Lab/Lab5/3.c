// Lab project by Sarang Dev Saha (20UCS173)
//LAB5_QUES 3
//Reading a four digit number from the keyboard and printing the sum of the digits.
#include <stdio.h>  

int main()
{
    int num1,num2,num3,num4,sum;
        
    // Reading a 4 digit number from the keyboard, but separating it into four variables
    printf("Enter a four-digit number: ");
    scanf("%1d%1d%1d%1d", &num1, &num2, &num3, &num4);
    
    // Adding the digits to get the sum.
    sum=num1+num2+num3+num4;
    
    printf("The expected output is: %d", sum);
    
    return 0;
}