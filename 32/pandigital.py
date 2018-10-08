"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital. The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from itertools import permutations


def pandigital(x,y,z):
    n = f"{x}{y}{z}"
    if len(n) != 9:
        return False
    if "0" in n:
        return False
    for num in n:
        if n.count(num) > 1:
            return False
    return True


all_list = []

for x in range(1, 5):
    for a_list in list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], x)):
        all_list.append(int("".join(map(str, a_list))))

total_sum = 0
pandigital_uniqs = []
count = 0
for x in all_list:
    for y in all_list:
        mult = x * y
        if pandigital(x,y,mult):
            if mult not in pandigital_uniqs:
                pandigital_uniqs.append(mult)
    count += 1
print(sum(pandigital_uniqs))
