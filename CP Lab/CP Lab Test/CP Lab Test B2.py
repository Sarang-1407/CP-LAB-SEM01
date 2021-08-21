#CP Lab Test by Sarang Dev Saha (Roll no. 20UCS173)

#Taking input from the user
num_raw=float(input("Enter a two-digit number:"))

#Forming 3 lists
#List1 is for 1-9, list2 is for 10-19 and list3 is for 20,30,40...90(list3 and list1 can be combined for the rest of the numbers)
list1=['','One','two','three','four','five','six','seven','eight','nine']
list2=['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
list3=['','','Twenty', 'Thirty','Forty','Fifty',' Sixty','Seventy','Eighty','Ninety']

#Converting the float input into int type as lists don't accept float value
num=int(num_raw)

#num1 gives the tenth's place of the number while num2 gives the one's place number.
num1=num//10
num2=num%10

#If input number is +ve
if num_raw>0:
    #When the number ranges from 1-9
    if num1==0:
        print("The number is ",num,"-",list1[num2])

    #When the number ranges from 10-19
    if num1==1:
        print("The number is ",num,"-",list2[num2])

    #When the number ranges from 20-99
    if num1>1:
        print("The number is ",num,"-",list3[num1]+'-'+list1[num2])

#If the input number is negative, we take its absolute value and proceed in the same way
if num_raw<0:
    num=int(-1*num_raw)
    num1=num//10
    num2=num%10
    
    #When the number ranges from 1-9
    if num1==0:
        print("The number is ",num,"-",list1[num2])

    #When the number ranges from 10-19
    if num1==1:
        print("The number is ",num,"-",list2[num2])

    #When the number ranges from 20-99
    if num1>1:
        print("The number is ",num,"-",list3[num1]+'-'+list1[num2])

    


