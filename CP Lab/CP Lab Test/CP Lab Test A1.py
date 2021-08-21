#Taking the input in seconds
seconds=float(input("Enter the time in seconds:"))

#Using floor division operator (//) to find the Greatest Integer function in each unit
minutes=seconds//60
hours=minutes//60
days=hours//24
years=days//365

#When input>=0, converting the time in years, days. hours, minutes and seconds by subtracting appropriately
if (seconds>=0):
    print("Years=",years,"Days=",days-365*years,"Hours=",hours-24*days,"Minutes=",minutes-60*hours,"Seconds=",seconds-60*minutes)

#When input<0, it is INVALID because time cannot be negative
if (seconds<0):
    print("INVALID")
