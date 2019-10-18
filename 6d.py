ip = input("Enter a string\n")
sp = ip.split()
for input in sp:
    print(input[::-1],end=" ")
print()
print(ip[::-1],end=" ")

