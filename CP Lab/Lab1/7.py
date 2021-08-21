# Lab Project by Sarang Dev Saha

# LAB_01 QUE_07
#A 30 kg boulder was initially moving at a velocity of 10 m/s, in order to stop it 10N of resistive force is applied on it. After how much time will the boulder come to rest

#Letting the user enter the above data
mass=float(input("Enter the mass of the object in kg:"))
initial_velocity=float(input("Enter the initial velocity of the object in m/s:"))
force=float(input("Enter the retarding force on the object in N:"))
#Formulating acceleration of the boulder
acceleration=(force/mass)
#Formulating time after which the boulder comes to rest. 
time=(initial_velocity)/acceleration
print("The object requires",time,"seconds to come to rest") 
