import math as m
x = int(input("Enter a number\n"))
add=0
mul=0
i=0
while i<=x:
	add=add+i
	i=i+1
mul = m.factorial(x)
print("Add = ",add)
print("Multiply = ",mul)
