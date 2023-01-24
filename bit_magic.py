def ispowerof2(n):
    # O(1)
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x, y

def bruteforce(n):
    # O(n)
    s = str(bin(n))[2:]
    print("{}", s)
    return(s.count('1'))

def cntbits(n):
    # O(log(n))
    cnt = 0
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt

t = int(input())
while t:
    n = int(input())
    print(ispowerof2(n))
    t = t-1