#include <stdio.h>
int main(){
    
    int number,i,sum;
    printf("Enter a number: ");
    scanf("%d",&number);
  
    if(isPerfect(number))
        printf("%d is a perfect number.",number);
    else
        printf("%d is not a perfect number.",number);
  
    return 0;
}

int isPerfect(int number)
{
    int i,sum;
    sum=0;
  
    for(i=1; i<number; i++)
    {
        if(number%i==0)
            sum+=i;
    }
     
    if(sum==number)
        return 1; /*Perfect Number*/
    else
        return 0; /*Not Perfect Number*/
}
 
 
