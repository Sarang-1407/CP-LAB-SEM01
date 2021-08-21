# Lab Project by Sarang Dev Saha

# LAB_02 QUE_07
#Take a string of 10 characters from the user and another string with 5 characters.Then print a string such that it conrains the first 5 characters from the first string and latter 5 characters from the second string.
 
#taking word from user
str1=input("Enter the 10 alphabet word here: ")

#error if limit exceeds or input is insufficient
if len(str1)>10:
    print("Error: The word should have exactly 10 alphabets")
    
elif len(str1)<10:
    print("Error: The word should have exactly 10 alphabets")
    
#printing the final strings    
else:
    part2=input("Enter the next 5 alphabets for the next word: ")
    str2=str1[0:5]+part2
    print(str1)
    print(str2)