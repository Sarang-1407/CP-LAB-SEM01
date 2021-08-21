# Lab Project by Sarang Dev Saha

# LAB_01 QUE_05
#Using a rope of fixed length, a circle, hexagon and an equilateral triangle are made, find their areas

#Taking input from the user
perimeter=float(input("Enter the length of the rope in meters:"))
#Formulating area of a circle
area_circle=(perimeter**2)/(4*22/7)
print("Area of the required circle=",area_circle,"sq. m")
#Formulating area of a regular hexagon
area_hexagon=(perimeter**2)/(192**0.5)
print("Area of the required hexagon=",area_hexagon,"sq. m")
#Formulating area of an equilateral triangle
area_triangle=(perimeter**2)/(432**0.5)
print("Area of the required Equilateral triangle=",area_triangle,"sq. m")
