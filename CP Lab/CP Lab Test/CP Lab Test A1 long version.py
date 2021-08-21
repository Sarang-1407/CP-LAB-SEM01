seconds=float(input("Enter the time in seconds:"))

minutes=seconds//60
hours=minutes//60
days=hours//24
years=days//365

if seconds<60:
    print("Years=0, Days=0, Hours=0, Minutes=0, Seconds=",seconds)

if (seconds>=60 and seconds<3600):
    print("Year=0, Days=0, Hours=0, Minutes=",minutes,"Seconds=", seconds-60*minutes)

if (seconds>=3600 and seconds<86400):
    print("Year=0, Days=0, Hours=",hours,"Minutes=", minutes-60*hours,"Seconds=", seconds-60*minutes)

if (seconds>=86400 and seconds<31536000):
    print("Year=0, Days=",days,"Hours=",hours-24*days,"Minutes=", minutes-60*hours,"Seconds=", seconds-60*minutes)

if (seconds>31536000):
    print("Year=",years, "Days=",days-365*years,"Hours=",hours-24*days,"Minutes=", minutes-60*hours,"Seconds=", seconds-60*minutes)

    
        
