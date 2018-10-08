"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

max = math.factorial(9)
total_sum = 0
facts = {}
for x in range(0,10):
    facts[x] = math.factorial(x)

for n in range(3,max):
    n_str = str(n)
    sum = 0
    for x in n_str:
       sum += facts[int(x)]
    if sum == n:
        total_sum += sum

print(f"Answer: {total_sum}")