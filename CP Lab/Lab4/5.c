#include <math.h>
#include <stdio.h>
int main() {
    float e_unit, amount, amount_tax;
    printf("Enter the amount of Electricity consumed:");
    scanf("%f", &e_unit);
    
    if (e_unit<=0){
        printf("The total Electricity bill is ₹0");
    }
    
    if (e_unit>0 && e_unit<=50){
        amount=(0.50*e_unit);
        amount_tax=(1.2*amount);
        printf("The total Electricity bill is ₹%f", amount_tax);
    }
    
    if (e_unit>50 && e_unit<=150){
        amount=(0.50*50+ 0.75*(e_unit-50));
        amount_tax=(1.2*amount);
        printf("The total Electricity bill is ₹%f", amount_tax);
    }
    
    if (e_unit>150 && e_unit<=250){
        amount=(0.50*50+ 0.75*100+ 1.20*(e_unit-150));
        amount_tax=(1.2*amount);
        printf("The total Electricity bill is ₹%f", amount_tax);
    }
    
    if (e_unit>250){
        amount=(0.50*50+ 0.75*100+ 1.20*100 +1.50*(e_unit-250));
        amount_tax=(1.2*amount);
        printf("The total Electricity bill is ₹%f", amount_tax);
    }


    

    return 0;
} 