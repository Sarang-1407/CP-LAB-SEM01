# Lab Project by Sarang Dev Saha

# LAB_02 QUE_07
#Take a string of 10 characters from the user and another string with 5 characters.Then print a string such that it conrains the first 5 characters from the first string and latter 5 characters from the second string. 

#Taking input from the user
str1=input("Enter a string of length 10:")
a=input("Enter a string of length 5:")
#Forming a string with the above mentioned rule
str2=str1[0:5]+a[0:5]
print("The new string is", str2)