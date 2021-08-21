// Lab project by Sarang Dev Saha (20UCS173)
//LAB6_QUES 
/* Write a program to print a half pyramid pattern. */
#include <stdio.h>

int main(){

	int num;
	printf("Enter number of persons: ");
	scanf("%d", &num);

	int arrAge[num];

	// This array will store the number of persons in each
	// age groups. We have taken total 7 age groups as given
	// in the begining of the code.
	// We initialize all the elements of the array with zero
	int freq[7]={0};

	int i=0;
	printf("Enter age after the prompt >>\n");

	int age;

	// We run the code for infinity so that if invalid age
	// is entered, it can be ignored until 'num' valid ages
	// are read from the keyboard
	for(;;){
	
		if(i>=num)
			break;
		printf(">> ");
		scanf("%d", &age);

		if(age <0 && age>150){
		
			printf("Enter a valid age\n");
		}
		else{
			arrAge[i] = age;
			i++;
		}

	}

	// Number of persons in each age group

	for(i=0; i<num; i++){
		
		if(arrAge[i] <=10)
			freq[0]++;
		else if(arrAge[i] <=20)
			freq[1]++;
		else if(arrAge[i] <= 30)
			freq[2]++;
		else if(arrAge[i] <= 40)
			freq[3]++;
		else if(arrAge[i] <= 50)
			freq[4]++;
		else if(arrAge[i] <=60)
			freq[5]++;
		else
			freq[6]++;

	}

	// Print frequency distribution for different age groups
	
	for (i=1; i<7; i++){
		
		printf("Persons below age %d are: %d\n", i*10+1, freq[i-1]);
		
	}
	printf("Persons above age 60 are: %d\n", freq[i-1]);

	// Frequency histogram (horizontal) 
	
	int j;
	printf("Printing Horizontal frequency histogram\n");
	printf("------------------------------------------------------\n");

	for(i=1; i<=7; i++){

		if(i<7)	
			printf("Age %2d-%2d ", (i-1)*10, i*10);
		else
			printf("Above  60 ");

		for(j=0; j<freq[i-1]; j++)
			printf(" * ");
		printf("\n");
	}

	printf("\n\n");
	printf("Printing Horizontal frequency histogram\n");
	printf("------------------------------------------------------\n");
	// Frequency histogram (Vertical)
	
	int max=0;
	for(i=0; i<7; i++)
		if(freq[i]>max)
			max = freq[i];

	for(i=max; i>0; i--){
	
		for(j=0; j<7; j++){
		
			if(freq[j] >= i)
				printf(" * ");
			else
				printf("   ");
		}
		printf("\n");
	}
}