# Lab Project by Sarang Dev Saha

# LAB_02 QUE_04
# Take a list of 10 nos. and remove 3rd to 6th elements and change the value of last element with a number taken from the user. 

list=[0, 1,2,3,4,5,6,7,8,9]
#Deleting 3,4,5 and 6 from the list
del list[3:7]
#printing the omitted list
print(list) 
# Entering input at the last position
list[5]=float(input("Enter new number:"))
print(list)