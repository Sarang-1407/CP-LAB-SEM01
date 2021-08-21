// Lab project by Sarang Dev Saha (20UCS173)
//LAB6_QUES 4
//Calculating the GCD of two numbers taken from the user.
#include <stdio.h>

int main() {
    int i,num1,num2,gcd;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);
// Using for loop with conditions on i (from 1 to either num1 or num2, whichever is smaller)
    for(i=1; i <= num1 || i <= num2; ++i)
    {
        // Checking if i is factor of both integers
        if(num1%i==0 && num2%i==0)
            gcd = i;
    }

    printf("GCD of %d and %d is %d", num1, num2, gcd);
    
    return 0;
}