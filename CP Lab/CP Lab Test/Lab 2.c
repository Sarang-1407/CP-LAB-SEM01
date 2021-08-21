// Name: Sarang Dev Saha
// Section: A2
// Roll no.: 20UCS173
// Date: 05/05/2021

#include <stdio.h>
int main(){
    //Reading 4 integers in an array ie. array[]
    int array[4];
    printf("Enter the 4 integers:");
    for(int i=0;i<4;++i){
        scanf("%d",&array[i]);
    }
    //introducing new variables to store the gcd of numbers using gcd() function
    //m and n are the numbers at places 1st and 3rd
    //a and b are numbers at places 2nd and 4th
    int m=array[0];
    int n=array[2];
    int a=array[1];
    int b=array[3];
    
    //Storing the output in an array ie. output[]
    int output[2];
    output[0]=gcd(m,n);
    output[1]=gcd(a,b);
    printf("GCD of the numbers are:");
    for(int j=0;j<2;++j){
        printf(" %d",output[j]);
    }
    return 0;

//Defining the function ie. gcd() case wise
}
int gcd(int x,int y){
    //If smaller number is 0 then gcd is the greater number
    if (y==0)
        return x;
    else
    //Else gcd is calculated using the given formula
        return gcd(y,x%y);
    
}
//end of program
//gcc 20ucs173.c
//gcc 20ucs173.c -o 20ucs173
//./20ucs173