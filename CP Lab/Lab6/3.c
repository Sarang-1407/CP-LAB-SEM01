// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 2
/* Write a program to print all palindromes between 1 and 100. */
# include <stdio.h>
int main() {
    int number,quotient,remainder;
	// Taking input from the user(optional)
	printf("Enter the number: ");
	scanf("%d",&number);
	//All single digit numbers are palindromes.
	if(number>0 && number<10){
		printf("The entered number is a Palindrome \n");
	}
	// Conditions for two-digit numbers to be palindromes (11,22,33,44,55,66,77,88,99)
	quotient=(number/10);
	remainder=(number%10);
	
	if(quotient==remainder){
		printf("The entered number is a Palindrome \n");
	}
	else{
	    printf("The entered number is NOT a Palindrome \n");
	}
	//Finally printing the list of palindromes between 1 and 100 
	printf("The Palindromes between 1 and 100 are 1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99 ");
	
    return 0;
}