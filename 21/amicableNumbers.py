__author__ = 'kmacarenco'

def d(x):
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum += i
    return sum
sum =0
for i in range (1,10000):
    n = d(i)
    n1 = d(n)
    if i == n1 and n1 != n:
        sum += i

print(sum)
