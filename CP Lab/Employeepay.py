print("Emplyee code: Clerk-1  Teacher-2  Principal-3")
role=int(input("Enter the Employee code:")) 
hour=float(input("Enter the total weekly hours:"))

if hour<=44:
	if role==1:
		print("The salary for this week is", hour*100,"$")
	if role==2:
		print("The salary for this week is", hour*200,"$")
	if role==3:
		print("The salary for this week is", hour*400,"$")
		
if hour>44 and hour<=50:
	if role==1:
		print("The salary for this week is",hour*100+ (hour-44)*2*100,"$")
	if role==2:
		print("The salary for this week is", hour*200+(hour-44) *2*200,"$")
	if role==3:
		print("The salary for this week is",hour*400+(hour-44) *2*400,"$")
		
if hour>50:
	if role==1:
		print("The salary for this week is",50*100+ (50-44)*2*100,"$")
	if role==2:
		print("The salary for this week is", 50*200+(50-44) *2*200,"$")
	if role==3:
		print("The salary for this week is", 50*400+(50-44) *2*400,"$")
	
	
	