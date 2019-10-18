n = int(input("Enter A Number"))
sum = 0
li = list()

for x in range(1,(n//2)+1):

	if n%x == 0:
		sum +=x

if sum == n:
	print("Perfect Number")
else:
	print("Not Perfect")
