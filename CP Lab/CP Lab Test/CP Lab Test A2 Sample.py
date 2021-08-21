distance=float(input("Enter the Total kilometers driven per day:"))
cost_petrol=float(input("Enter the Cost per litre of petrol:"))
mileage=float(input("Enter the Average kms per litre (mileage):"))
fee_parking=float(input("Enter the Parking fee per day:"))
toll=float(input("Enter the Toll tax per day:"))

if (distance>=0 and cost_petrol>=0 and mileage>0 and fee_parking>=0 and toll>=0):
    quantity_petrol=(distance/mileage)
    total_petrol=(quantity_petrol*cost_petrol)

    total_cost=toll+fee_parking+total_petrol

    print("The Total Cost of driving per day is ₹",total_cost)


if (distance<0 or cost_petrol<0 or mileage<=0 or fee_parking<0 or toll<0):
    print("INVALID input")
    
