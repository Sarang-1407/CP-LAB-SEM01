displacement= int(input("Enter the displacement traversed by the object in meters:"))
initial_velocity= int(input("Enter the initial velocity of the object:"))
acceleration= int(input("Enter the acceleration of the object:"))
time=(((initial_velocity)**2+2*acceleration*displacement)**0.5-initial_velocity)/acceleration
print("The time required is", time, "seconds")