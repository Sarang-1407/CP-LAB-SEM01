// CP Lab Mock Test by Sarang Dev Saha (20UCS173)
//CP LAB_MOCK
// Write a program to read and add two numbers

#include <stdio.h>
int main() {
    float num1, num2,sum;
    printf("Enter the two numbers to be added: ");
    scanf("%f%f", &num1,&num2);

    // Adding the two numbers
	sum=num1+num2;
    
    printf("The sum of the two numbers is %f", sum);
    
    return 0;
}