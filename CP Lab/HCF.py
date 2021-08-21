a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
	lesser=b
else:
	lesser=a
for c in range(1, lesser+1):
	if((a%c==0) and (b%c==0)):
		hcf= c
print("The HCF of the numbers is",c)