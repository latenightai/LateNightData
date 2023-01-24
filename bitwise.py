# & : and
# | : or
# ~ : not
# ^ : xor
# >> : right shift : divide in power of 2
# << : left shift : multiply in power of 2

def evenodd(n):
    if n&1 == 1:
        print("odd")
    else:
        print("even")

t = int(input())
while t:
    n = int(input())
    evenodd(n)
    t = t-1