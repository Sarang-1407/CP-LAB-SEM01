# Lab Project by Sarang Dev Saha

# LAB_02 QUE_08
# Take 3 numbers from the user and print the second largest and largest number without using any iterative statements and inbuilt functions. 

# Taking 3 numbers from user
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
#When a is the second largest number
if (a>b or a>c or c>a or c>b or b>c or b>a):
	if (c>a and a>b) or (b>a and a>c):
		print("The second largest number is", a)
#When b is the second largest number
	if (b>a and c>b) or (b>c and a>b):
		print("The second largest number is", b)	
#When c is the second largest number
	if (b>c and c>a) or (a>c and c>b):
		print("The second largest number is", c)
#When a is the largest number
if (a>b and a>c):
	print("The largest number is",a)
#When b is the largest number
if (b>c):
	print("The largest number is",b)
#When c is the largest number
else:
	print("The largest number is",c)