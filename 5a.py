n = int(input("Enter a Number : "))
li = []

for x in range(1,(n//2)+1):

	if n%x == 0:
		li.append(x)
li.append(n)
if (len(li)>2):
	print("Not A Prime")
	print(li)
else:
	print("Prime Number")
	print(li)
