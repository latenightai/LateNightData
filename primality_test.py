from math import *

def a1(n):
    divcnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            divcnt += 1
    print(divcnt)
    if divcnt == 2:
        return True 
    else:
        return False 

def a2(n):
    if n ==0 or n == 1:
        return False
    if n ==2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    for i in range(3, int(sqrt(n))+1):
        if n%1 == 0 or n%(i+2) == 0:
            return False

t = int(input())
while(t):
    n = int(input())
    print(a1(n))
    print(a2(n))
    t = t-1
