# Lab Project by Sarang Dev Saha

# LAB_01 QUE_04
#Write a python program to calculate the time required for a car to traverse 5 km starting from rest with acceleration 30 m/s2 

#Using the data from the question. 
initial_velocity=0;
displacement=5000;
acceleration=30;
#Formulating time using s=ut+1/2(at^2)
time=(((initial_velocity)**2+2*acceleration*displacement)**0.5 - initial_velocity)/acceleration
print("The time required is", time, "seconds") 
