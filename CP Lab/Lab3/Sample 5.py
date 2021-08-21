#SAMPLE CODE
#THIS CODE IS NOT COMPLETE AND HAS SOME FAULT IN IT'S EXECUTION 

month=[" ","Jan","Feb","March","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
date=input("Enter a date in DD-MM-YYYY format:")
month_str=date.split('-')[1]
month_int=int(month_str)
month_name=month[month_int]
year=int(date.split('-')[2]) 
if month_int==1 or 3 or 5 or 7 or 8 or 10 or 12:
	print("The month is", month_name, "and it has 31 days") 
if month_int==4 or 6 or 9 or 11:
	print(" The month is", month_name, "and it has 30 days")
if month_int==2:
      if year%4==0:
      	print("The month is", month_name, "and this is a LEAP year, hence it has 29 days")
	
	
