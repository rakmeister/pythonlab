import math as m
n = int(input("Enter the number: "))
root = m.sqrt(n)
i = 0
f = 0
if root == int(root):
    print("Perfect Square")
else:
    print("Not A Perfect Square")

while i <= n/2:
    if 2**i == n:
        print("Power of 2")
        f = 1
    i = i+1

if f == 0:
    print("Not power of 2")


def fib(a):
    l = 0
    u = 1
    while True:
        if u == a:
            return 1
        if u > a:
            return 0
        temp = u
        u = u+l
        l = temp


if fib(n) == 1:
    print("Present in the series")
else:
    print("Not present in the series")
