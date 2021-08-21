# Lab Project by Sarang Dev Saha

# LAB_02 QUE_03
# Take a number from the user and print its absolute value. 

# Taking input from user
number=float(input("Enter the number:"))
# If number is negative
if number<0:
	abs_num=-number
	print("The absolute value of the entered number is",abs_num)
# If number is positive
else:
	print("The absolute value of the entered number is",number)