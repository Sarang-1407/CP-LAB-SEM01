# Lab Project by Sarang Dev Saha

# LAB_02 QUE_01
# A shopkeeper gives a discount of 10% if the bill amount is more than ₹1000, or else the undiscounted price is to be printed. 

print("A can of soda costs ₹50")
# Taking quantity of items from the user
quantity=int(input("Enter the number of cans:"))
# Formulating the total amount
amt=50*quantity
# In case amount is greater than 1000
if amt>1000:
	fin_amt=0.9*amt
	print("The total payable amount is ₹",fin_amt)
#In case amount is lesser than 1000
else:
	print("The total payable amount is ₹",amt)