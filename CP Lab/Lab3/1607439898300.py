# Lab Project by Sarang Dev Saha 

# LAB_03 QUE_05
#Write a program that reads date from the user in DD-MM-YYYY format and prints the number of days in that month, even considering case of a leap year. 

#Forming a list of all the months according to their numerical order. 
month=[" ","Jan","Feb","March","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#Taking the date from the user
date=input("Enter a date in DD-MM-YYYY format:")
#Splitting the date in a list and selecting the month
month_num=date.split('-')[1]
#Converting string into int and selecting the name of the month from the list
month_name=month[int(month_num)]
year=int(date.split('-')[2]) 

#Condition for the month to have 31 days
if (month_name =='Jan' or month_name =='March' or month_name =='May' or month_name =='Jul' or month_name =='Aug' or month_name =='Oct' or month_name =='Dec'):
	print("The month is", month_name, "and it has 31 days") 
	
#Condition for the month to have 30 days
if (month_name=='Apr' or month_name =='June' or month_name =='Sep' or month_name =='Nov'):
	print("The month is", month_name, "and it has 30 days")
	
#If the month is February we have 2 more cases
if (month_name=='Feb'):
      if (((year%4==0) and (year%100!=0)) or (year%400==0)):
      	print("The month is", month_name, "and this is a LEAP year, hence it has 29 days")
      else:
      	print("The month is",month_name, " and this is a NON-LEAP year, hence it has 28 days")
      	
	
	
