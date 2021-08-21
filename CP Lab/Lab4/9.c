// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 9
/* Read three numbers from the keyboard. Find the maximum and second maximum
of these numbers. */
# include <stdio.h>
int main() {
    double n1, n2, n3;
    printf("Enter the three numbers: ");
    scanf("%lf %lf %lf", &n1, &n2, &n3);

    // when n1 is the greatest and if n2 or n3 is second largest
    if (n1 >= n2 && n1 >= n3){
        printf("%.2f is the largest number\n", n1);
		if (n2>=n3){
			printf("%2f is the second largest number", n2);
		}
		
		else{
			printf("%2f is the second largest number", n3);
		}
    }

    // if n2 is the greatest and if n1 or n3 is the second largest
    if (n2 >= n1 && n2 >= n3){
        printf("%.2f is the largest number\n", n2);
		if (n1>=n3){
			printf("%2f is the second largest number", n1);
		}
		
		else{
			printf("%2f is the second largest number", n3);
		}
    }

    // if n3 is greatest and if n1 or n2 is the second largest
    if (n3 >= n1 && n3 >= n2){
        printf("%.2f is the largest number\n", n3);
		if (n1>=n2){
			printf("%2f is the second largest number", n1);
		}
		
		else{
			printf("%2f is the second largest number", n2);
		}
    }

    return 0;
}