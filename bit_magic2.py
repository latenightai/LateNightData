def intToBin(n):
    return str(bin(n))[2:]

def bitnToInt(s):
    return int(s, 2)

def kthbit(n, k):
    print(str(bin(n))[2:])
    if n & (1 << (k-1)):
        print("SET")
    else:
        print("NOT SET")

def find_single_occur(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    return res

t = int(input())
while t:
    arr = list(map(int, input().split()))
    
    n = int(input())
    binstring = intToBin(n)
    integer = bitnToInt(n)
    print(n, binstring, integer, n == integer)
