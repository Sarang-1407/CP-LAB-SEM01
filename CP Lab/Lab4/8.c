// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 8
// Take any number as user input and print whether it is an even number or odd.
#include <stdio.h>
int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);

    // If num is perfectly divisible by 2
    if(num % 2 == 0)
        printf("The number is EVEN.", num);
    else
        printf("The number is ODD.", num);
    
    return 0;
}