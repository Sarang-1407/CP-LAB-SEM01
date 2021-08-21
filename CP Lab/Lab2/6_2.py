# Lab Project by Sarang Dev Saha

# LAB_02 QUE_06
#Take a list of 5 numbers and print the maximum number. 

#we first take 5 number as input
num1=int(input("entre value of number1:"))
num2=int(input("entre value of number2:"))
num3=int(input("entre value of number3:"))
num4=int(input("entre value of number4:"))
num5=int(input("entre value of number5:"))
#we make a list which contain all the 5 numbers
list=[num1,num2,num3,num4,num5]
#now we need to find the maximum among these 5 numberss.
#for this we use if and else statement.
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
   print("The greatest number is",num1)
#the above statement confirm that num1 is greatest number or not.   
elif num2>num3 and num2>num4 and num2>num5:
   print("The greatest number is",num2)
#the above statement confirm that num2 is   greatest number or not.
elif num3>num4 and num3>num5:
   print("The greatest number is",num3)
#the above statement confirm that num3 is greatest number or not.
elif num4>num5:
    print("The greatest number is",num4)
#the above statement confirm that num4 is greatest number or not.
#if  all the above statement is false then num5 is the greatest number.
else:
    print("The greatest number is",num5)
