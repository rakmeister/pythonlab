import math as m
a = float(input("Enter the value of a\n"))
b = float(input("Enter the value of b\n"))
c = float(input("Enter the value of c\n"))
d = b*b-4*a*c
if d>0:
	print("Roots are Real and Distinct\n")
	r1 = ((-b+m.sqrt(d))/(2*a))
	r2 = ((-b-m.sqrt(d))/(2*a))
	print(r1,r2)
elif d==0:
	print("Roots are Real and Equal\n")
	r = -b/(2*a)
	print(r)
else :
	real=b/(2*a)
	img = ((m.sqrt(-1*d))/(2*a))
	print("The Roots are Imaginary\n")
	print(real,"+",img,"i")
	print(real,"-",img,"i")  
