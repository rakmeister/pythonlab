a=float(input("Enter 1st number :"))
b=float(input("Enter 2nd number :"))
print("1.Addition\n2.Subtract\n3.Multiply\n4.Divide")
op=int(input("Choose the opertion :"))
if(op==1):
	print(a,"+",b,"=",a+b)
elif(op==2):
	print(a,"-",b,"=",a-b)
elif(op==3):
	print(a,"*",b,"=",a*b)
elif(op==4):
	print(a,"/",b,"=",a/b)
else:
	print("Invalid Choice")
