n = int(input())

sum =n*(n+1)/2
print(sum)

# o(1)

#### using while loop ###

while(n>0):
    sum += n
    n -= 1

print(sum)

#### using for loop ####
sum = 0
for i in range(1, n+1):
    sum += i

print(sum)