word1 = input("Enter the text")
print(len(word1))
x = len(word1)
i=0
a=0
d=0
s=0
r=0
for i in range(0,x):
    if word1[i].isalpha():
        a+=1
    elif word1[i].isdigit():
        d+=1 
    elif word1[i].isspace():
        s+=1
    else:
        r+=1  
print("No of alphabets ",a)
print("No of digits",d)
print("No of Special Characters",r)
