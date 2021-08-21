# Lab Project by Sarang Dev Saha

# LAB_02 QUE_06
#Take a list of 5 numbers and print the maximum number. 

#empty list
lst = []
#Taking input from user
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))