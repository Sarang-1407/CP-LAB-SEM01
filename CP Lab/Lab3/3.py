# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_03
#Write a program to input sides of a triangle and check whether triangle is valid or not

#Taking input from the user
side1=float(input("Enter the length of side 1:"))
side2=float(input("Enter the length of side 2:"))
side3=float(input("Enter the length of side 3:"))
#A triangle is valid as long as the sum of two sides is greater than the third
#Condition for the validity of the triangle
if (side1+side2>side3) and (side2+side3>side1) and (side3+side1>side2):
	print("The above mentioned sides are VALID for a triangle")
#Condition for the invalidity of the triangle
else:
	print("The above mentioned sides are INVALID for a triangle")