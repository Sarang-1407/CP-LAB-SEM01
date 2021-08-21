# include <stdio.h>

int main(){
    
    float perimeter, area_circle, area_hex, area_tri;

    
    printf("Enter the chosen Perimeter:");
    scanf("%f", &perimeter);
    area_circle= (perimeter*perimeter)/(4*3.14);
    area_hex= (perimeter*perimeter)/sqrt(192);
    area_tri= (perimeter*perimeter)/sqrt(432);
    printf("The Area of Circle is %f \n",area_circle);
    printf("The Area of Hexagon is %f \n",area_hex);
    printf("The Area of Triangle %f \n",area_tri);
    
    return 0;
}