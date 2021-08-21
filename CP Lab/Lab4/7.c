// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 7
// Reading 2 numbers from the keyboard and comparing them.
# include <stdio.h>

int main(){
    
    float num1,num2;
    printf("Enter the two numbers:");
    scanf("%f%f",&num1,&num2);
	
	// There are 3 cases ie. when num1 is greater or num2 is greater or when both are equal.
    if (num1>num2){
        printf("The first number is the greater one ie.%f", num1);
    }
    
    else if (num2>num1){
        printf("The second number is the greater one ie.%f", num2);
    }
    else{
        printf("Both numbers are equal to %f", num1);
    }
    
    
    return 0;
}