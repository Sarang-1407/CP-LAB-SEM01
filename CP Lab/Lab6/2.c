// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 2
/* Read two single digit numbers and calculate first number raised to the power
second number. */
# include <stdio.h>
# include <math.h> //using math.h header to accomodate pow() function
int main() {
    float a,b, number;
	//Taking the numbers from the user
	printf("Enter a single digit number: ");
	scanf("%f",&a);
	printf("Enter another single digit number: ");
	scanf("%f",&b);
	//using pow() function to calculate the power of the number.
    number= pow(a,b);
	printf("The resulting number is %f",number);
    return 0;
}