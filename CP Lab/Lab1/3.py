a=input("Enter the name of the Students:")
names =[name.upper() for name in a.split()]
names.sort()
print("The alphabetically arranged names are:")
for name in names:
   print(name)
