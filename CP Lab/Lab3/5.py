# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_05
#Write a program that reads date from the user in DD-MM-YYYY format and prints the number of days in that month, even considering case of a leap year. 

#Forming a list of all the months according to their numerical order. 
month=[" ","January","February","March","April","May","June","July","August","September","October","November","December"]
#Taking the date from the user
date=input("Enter a date in DD-MM-YYYY format:")
#Splitting the input data using '-' as a separator and selecting the month
month_num=date.split('-')[1]
#Converting string into int and selecting the name of the month from the list
month_name=month[int(month_num)]
year=int(date.split('-')[2]) 
day=int(date.split('-')[0])

#Condition for the month to have 31 days
if (month_name =='January') or (month_name =='March') or (month_name =='May') or (month_name =='July') or (month_name =='August') or (month_name =='October') or (month_name == 'December'):
	if day<=31:
		print("The month is", month_name, "and it has 31 days") 
	elif day>31:
		print(" This is an INVALID date")
	
#Condition for the month to have 30 days
if (month_name=='April') or (month_name == 'June' ) or (month_name =='September') or (month_name =='November'):
	if day<=30:
		print("The month is", month_name, "and it has 30 days")
	elif day>30:
		print(" This is an INVALID date")
	
#If the month is February we have 2 more cases of leap and non-leap year
if (month_name=='February'):
      if (((year%4==0) and (year%100!=0)) or (year%400==0)):
      	if day<=29:
      		print("The month is", month_name, "and this is a LEAP year, hence it has 29 days")
      	elif day>29:
      		print(" This is an INVALID date")
      else:
      	if day<=28:
      		print("The month is",month_name, " and this is a NON-LEAP year, hence it has 28 days")
      	elif day>28:
      		print(" This is an INVALID date")
      	
	
	
