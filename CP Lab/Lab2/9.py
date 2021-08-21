# Lab Project by Sarang Dev Saha

# LAB_02 QUE_09
#Read a single digit number from the keyboard and print its corresponding day of week. If number other than 1-7 is entered, print “Invalid Number".

#Taking input fromcthe user
a=int(input("Enter a single digit number:"))
#Using if function to assign a specific day to a number from 1-7
if a==1:
	print("It is Monday")
if a==2:
	print("It is Tuesday")
if a==3:
	print("It is Wednesday")
if a==4:
	print("It is Thursday")
if a==5:
	print("It is Friday")
if a==6:
	print("It is Saturday")
if a==7:
	print("It is Sunday")
else:
	print("Invalid Number")

