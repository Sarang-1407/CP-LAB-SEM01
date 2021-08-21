# Lab Project by Sarang Dev Saha

# LAB_01 QUE_03
#Read names of two students and print them in alphabetical order

#Taking input from the user
names = input("Enter the name of the students:")
#Separating the names using split() function
x = names.split()
#Arranging the names in ascending order using sort() function
x.sort()
print(x)
