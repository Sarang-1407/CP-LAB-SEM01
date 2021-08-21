# Lab Project by Sarang Dev Saha

# LAB_01 QUE_06
# The perimeter of a circle, square and an equilateral triangle is the same and taken from the user, calculate their respective areas. 

#Taking input from the user
perimeter=float(input("Enter the Perimeter in meters:"))
#Formulating area of a Circle
area_circle=(perimeter**2)/(4*22/7)
#Formulating area of a Square
area_square=(perimeter**2)/16
#Formulating area of an equilateral triangle
area_triangle=(perimeter**2)/(432**0.5)
print("Area of the required Circle=",area_circle,"sq. meters")
print("Area of the required Square=",area_square,"sq. meters")
print("Area of the required Equilateral Triangle=",area_triangle,"sq. meters")

