# Lab Project by Sarang Dev Saha

# LAB_02 QUE_05
# Take 2 strings from the user. If String1 is present in String2 then print so, else print 'Not found'. 

# Taking both inputs from the user
string1=input("Enter first string:")
string2=input("Enter second string:")
# If string1 is present in string 2
if string1 in string2:
	print("string1 is present in string2")
# If string1 is not present in string2
else:
	print("Not found")