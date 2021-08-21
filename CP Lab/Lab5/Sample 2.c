#include <stdio.h>  

int main(void)
{
    int num1, num2, num3, num4;
        
    // Reading a 2 digit number from the keyboard, but separating it into two variables

    printf("Enter a four-digit number: ");
    scanf("%1d%1d%1d%1d", &num1, &num2, &num3, &num4);
    printf("The desired output is: %1d%1d%1d%1d", &num4, &num3, &num2, &num1);
    return 0;
}