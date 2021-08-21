# Lab Project by Sarang Dev Saha

# LAB_01 QUE_01
#Take two numbers as user input and print the maximum number

#Taking input fromcthe user
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
#If a is greater than b
if a>b:
    print("a is the greater number:",a)
#If b is greater than a
elif a<b:
    print("b is the greater number:",b)
#If both a and b are equal
else:
    print("Both a and b are equal:",a)
    
