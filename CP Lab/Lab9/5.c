#include <stdio.h>
 
#include <string.h>
 
int main()
 
{
 
   int i, j, num=10;
 
   char name[20][10], t_name[15][10], temp[20];
 
 
 
   printf("10 names are to be sorted in alphabetical order\n");
 
  printf("Please enter %d names one by one\n", num);
 
   for(i=0; i< 10 ; i++)
 
   {
 
      scanf("%s",name[i]);
 
      strcpy (t_name[i], name[i]);
 
   }
 
 
 
   for(i=0; i < 9 ; i++)
 
   {
 
      for(j=i+1; j< 10; j++)
 
      {
 
         if(strcmp(name[i],name[j]) > 0)
 
         {
 
             strcpy(temp,name[i]);
 
             strcpy(name[i],name[j]);
 
             strcpy(name[j],temp);
 
         }
 
      }
 
   }
 
 
 
   printf("Names before sorting in alphabetical order\n");
 
   for(i=0; i< 10 ; i++)
 
   {
 
      printf("%s\n",t_name[i]);
 
   } 
 
 
 
   printf("Names after sorting in alphabetical order\n");
 
   for(i=0; i< 10 ; i++)
 
   {
 
      printf("%s\n",name[i]);
 
   }
 
   
 
}