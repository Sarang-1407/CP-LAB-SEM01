// Lab project by Sarang Dev Saha (20UCS173)
//LAB5_QUES 2
//Reading a four digit number from the keyboard and reversing it's order.
#include <stdio.h>  

int main()
{
    int num1,num2,num3,num4;
        
    // Reading a 4 digit number from the keyboard, but separating it into four variables
    printf("Enter a four-digit number: ");
    scanf("%1d%1d%1d%1d", &num1, &num2, &num3, &num4);
    
    // In order to reverse the order of the digits we apply the required formula.
    int new_num1,new_num2,new_num3,new_num4, output;
    new_num1= num4*1000;
    new_num2=num3*100;
    new_num3=num2*10;
    new_num4=num1*1;
    output= (new_num4+new_num3+new_num2+new_num1);
    
    printf("The expected output is: %d", output);
    
    return 0;
}