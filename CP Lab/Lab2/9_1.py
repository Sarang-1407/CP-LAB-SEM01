# Lab Project by Sarang Dev Saha

# LAB_02 QUE_09
#Read a single digit number from the keyboard and print its corresponding day of week. If number other than 1-7 is entered, print “Invalid Number".

# Forming list of all the days in a week
list=[" " ,'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Taking a number from the user
a=int(input("Enter a single digit number:"))
# If number is less than or equal to 7
if a<=7:
	print("The day of the week is",list[a]) 
else:
# Else error message is displayed
	print("Invalid Number")