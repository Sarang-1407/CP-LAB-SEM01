# Lab Project by Sarang Dev Saha

# LAB_02 QUE_08
# Take 3 numbers from the user and print the second largest and largest number without using any iterative statements and inbuilt functions. 

# Taking 3 numbers from user
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
list=[a, b, c]
# Using sort() function to arrange numbers in ascending order
list. sort() 
# Printing Maximum number
print("Maximum number is",list[2])
# Printing second maximum number
print("Second Maximum number is",list[1])