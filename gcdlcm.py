# for gcd using euclid formula
# for lcm: product(a, b) = lcm x gcd 

t = int(input())

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    prod = a*b
    hcf = gcd(a,b)
    return prod // hcf
while t:
    n, m = map(int(input().split()))
    print("gcd = {} lcm = {}".format(gcd(n, m), lcm(n, m)))
    t -= 1