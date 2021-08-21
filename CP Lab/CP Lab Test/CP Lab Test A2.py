#CP Programming Lab Evaluation 1 by Sarang Dev Saha (Roll no.-20UCS173) Section A2
#Date- 08/01/2021

#This is a program that calculates your daily driving cost, so that you can estimate how much money could be saved.

#Taking the given input from the user
distance=float(input("Enter the Total Kilometers driven per day:"))
cost_petrol=float(input("Enter the Cost per litre of petrol:"))
mileage=float(input("Enter the Average kms per litre (mileage):"))
fee_parking=float(input("Enter the Parking fee per day:"))
toll=float(input("Enter the Toll tax per day:"))

#The operation is VALID when the inputs are greater than equal to 0 and greater than 0 in case of mileage
#(mileage can't be 0 as quantity_petrol will be undefined)
if (distance>=0 and cost_petrol>=0 and mileage>0 and fee_parking>=0 and toll>=0):
    #Quantity of petrol is (distance/mileage)
    quantity_petrol=(distance/mileage)
    #total petrol is (quantity of petrolxcost of petrol) 
    total_petrol=(quantity_petrol*cost_petrol)
    
    #Total cost of driving per day is (total cost of petrol+parking fee+toll)
    total_cost=(toll+fee_parking+total_petrol)
    print("The Total Cost of driving per day is Rs.",total_cost)
    
#The operation is INVALID when the inputs are negative (even if mileage is 0 the output is INVALID)
if (distance<0 or cost_petrol<0 or mileage<=0 or fee_parking<0 or toll<0):
    print("INVALID input")
