# Lab Project by Sarang Dev Saha 

# LAB_02 QUE_02
# Take the marks scored my the student and assign him a grade for the same. 

# Taking the marks scored by the student from the user
marks=float(input("Enter the marks obtained:"))
# If marks is less than 25, the student gets a F grade
if marks<25:
	print("The candidate has got a F grade")
# If marks is less than 25, the student gets an E grade
if marks<45 and marks>=25:
	print("The candidate has got an E grade")
# If marks is less than 25, the student gets a D grade
if marks<50 and marks>=45:
	print("The candidate has got a D grade")
# If marks is less than 25, the student gets a C grade
if marks<60 and marks>=50:
	print("The candidate has got a C grade")
# If marks is less than 25, the student gets a B grade
if marks<80 and marks>=60:
	print("The candidate has got a B grade")
# If marks is less than 25, the student gets an A grade
if marks>=80:
	print("The candidate has got an A grade")