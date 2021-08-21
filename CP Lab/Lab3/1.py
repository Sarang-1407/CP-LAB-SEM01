# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_01
#Write a program to find all roots of a quadratic equation, take the values of a, b, c and print the roots. 

#Giving the user a gist of quadratic equations
print("A quadratic equation is in the form ax²+bx+c=0")
#Taking the values of a, b and c from the user
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
#The formula for calculating roots of a quadratic equation
root_1=(-b+(b**2-4*a*c)**0.5)/2*a
root_2=(-b-(b**2-4*a*c)**0.5)/2*a
print("The roots of the quadratic equation are", root_1,"and",root_2)