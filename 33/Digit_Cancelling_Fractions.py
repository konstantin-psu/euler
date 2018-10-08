"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
noms = []
denoms = []
def common_digit(nom, denom):
    nom_str = str(nom)
    denom_str = str(denom)
    nom_count = 0
    denom_count = 0
    found = False
    for n in nom_str:
        for d in denom_str:
            if n == d:
                found = True
                break
            denom_count+=1
        if found:
            break
        denom_count = 0
        nom_count += 1
    if found:
        # print(f"common {nom}/{denom}: common :{nom_str[nom_count]}")
        if nom_count == 0:
            nom_count = 1
        else:
            nom_count = 0
        if denom_count == 0:
            denom_count = 1
        else:
            denom_count = 0
        short_nom = int(nom_str[nom_count])
        short_denom = int(denom_str[denom_count])
        if short_nom == 0 or short_denom == 0:
            return
        if nom % 10 == 0 and denom % 10 ==0:
            return
        if nom / denom == short_nom / short_denom:
            print(f"NonTrivial Fraction {nom}/{denom}")
            noms.append(nom)
            denoms.append(denom)


for nominator in range(10,100):
    for denominator in range (10, 100):
        if nominator >= denominator:
            continue
        common_digit(nominator, denominator)

from functools import reduce

nomp = reduce((lambda x, y: x * y), noms)
denomp = reduce((lambda x, y: x * y), denoms)

print(f"Product {nomp}/{denomp}")
print(f"Answer {denomp/nomp}")
