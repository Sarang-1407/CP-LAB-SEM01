// Online C compiler to run C program online
#include <stdio.h>

int main() {
    char option;
    struct book{
        int ID;
        char title;
        char author;
        int isIssued;
        
    }
    printf("Welcome to LNMIIT Library Access \n Choose one of the following \n");
    printf(" a. Add Book \n b. Display \n c. Issue a Book \n d. Exit Menu \n");
    printf("Enter your option:");
    scanf("%c",&option);
    
    if (option=='d'||option=='D'){
        printf("Good-Bye");
    }
    
    if (option)
    return 0;
}