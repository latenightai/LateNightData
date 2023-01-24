from math import *

# O(root(n))
def divisors(n):
    div = set()
    for i in range(1, int(sqrt(n))+1):
        if n%i == 0:
            div.add(i)
            div.add(n//i)

    return list(div)


"""
a = [1, 2, 34, 5, 5]
for i in range(0, len(a)):
    print(a[i], end=" ")

simpler form:
print(*a)
"""