# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_04
#Write a program to input electricity unit charge and calculate the total electricity bill according to the given conditions...An additional surcharge of 20% is added to the bill

#Taking the input from the user
e_unit=float(input("Enter the Electricity Unit Charge consumed:"))

#If the input is less than equal to 0 the bill is also ₹0
if e_unit<=0:
		print("The total electricity bill including 20% surcharge is ₹0") 
	
#If the input is between 0 and 50
if e_unit>0 and e_unit<=50:
	amount=e_unit*0.50
	amount_tax=1.2*amount
	print("The total electricity bill including 20% surcharge is ₹",amount_tax)
	
#If the input is between 50 and 150	
if e_unit>50 and e_unit<=150:
	amount=(50*0.50)+(e_unit-50)*0.75
	amount_tax=1.2*amount
	print("The total electricity bill including 20% surcharge is ₹",amount_tax)
	
#If the input is between 150 and 250	
if e_unit>150 and e_unit<=250:
	amount=(50*0.50)+(100*0.75)+(e_unit-150)*1.20
	amount_tax=1.2*amount
	print("The total electricity bill including 20% surcharge is ₹",amount_tax)
	
#If the input is greater than 250 (else command can also be used, but triggers some glitch) 	
if e_unit>250:
	amount=e_unit*1.50
	amount_tax=1.2*amount
	print("The total electricity bill including 20% surcharge is ₹",amount_tax)