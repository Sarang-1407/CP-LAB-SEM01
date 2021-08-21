#include <stdio.h>

int main() {
    int i, number,sum;
    printf("Enter a number:");
    scanf("%d",&number);
    sum=0;
    for(i=1;i<number;i++){
        if (number%i==0)
            sum+=i;
    }
        if (sum==number)
            printf("This is a perfect number");
        else
            printf("This is not a perfect number");
        
    return 0;
}