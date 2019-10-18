a = ['radar','hello','rocky','bob','mom']
c=0
for i in a:
    if len(i)>=2 and i[0]==i[-1]:
        c=c+1
print(c) 