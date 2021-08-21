# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_02
#Read a number from keyboard and print it’s integral and fractional part separately

#Taking the input from the user
number=float(input("Enter a number:")) 
#Assigning a variable the value of integral part of the number
int_number=int(number)
#Assigning another variable the value of fractional part of the number
frac_number=float(number)-int(number)
print("The integral part of the number is",int_number)
print("The fractional part of the number is",frac_number)