#CP Lab Test by Sarang Dev Saha (Roll. no.- 20UCS173)

#Taking input from the user
distance=float(input("Enter Total distance travelled in KMs:"))
time=float(input("Enter Time travelled in minutes:"))

#When distance is negative the case is INVALID.
if (distance<0):
    print("INVALID")

#When time is negative the Case is INVALID. 
if (time<0):
    print("INVALID")

#When distance and time both are 0, some amount is still charged ie. Rs. 100.
if (distance==0) and (time==0):
    print("Total Bill amount is Rs. 100")

#When distance is 0 and if time>0, some waiting charge is accounted for, with 2 cases when time<10 or time>10
if (distance==0):
    if (time<10):
        print("Total Bill amount is Rs. 100")
    if (time>10):
        bill=100+ 1.5*(time-10)
        print("Total Bill amount is Rs. ",bill)
    
#If distance is between 0 and 12 and whether time is less than or greater than 10
if (distance>0 and distance<=12):
    if (time<=10):
        print("Total Bill amount is Rs. 100")
    if (time>10):
        bill=100+1.5*(time-10)
        print("Total Bill amount is Rs. ",bill)

#If distance is between 12 and 16 and whether time is less than or greater than 10
if (distance>12 and distance<=16):
    if (time<=10):
        bill=100+8*(distance-12)
        print("Total Bill amount is Rs. ",bill)
    if (time>10):
        bill=100+8*(distance-12)+1.5*(time-10)
        print("Total Bill amount is Rs. ",bill)

#If distance is between 16 and 20 and whether time is less than or greater than 10
if (distance>16 and distance<=20):
    if (time<=10):
        bill=100+8*(4)+ 6*(distance-16)
        print("Total Bill amount is Rs. ",bill)
    if (time>10):
        bill=100+8*(4)+6*(distance-16)+1.5*(time-10)
        print("Total Bill amount is Rs. ",bill)

#If distance is greater than 20 and whether time is less than or greater than 10
if (distance>20):
    if (time<=10):
        bill=100+8*(4)+ 6*(4)+5*(distance-20)
        print("Total Bill amount is Rs. ",bill)
    if (time>10):
        bill=100+8*(4)+ 6*(4)+5*(distance-20)+1.5*(time-10)
        print("Total Bill amount is Rs. ",bill)
