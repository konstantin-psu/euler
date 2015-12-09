__author__ = 'kmacarenco'

ma = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = 0
totalcount  = 3  # Jan first of 1901 was Tuesday
start = 1901
end = 2001
for y in range(start, end):
    for d in ma:
        if d == 28 and y % 4 == 0:
            d = 29
        for i in range(d):
            if totalcount % 7 == 0 and i == 0:
                count += 1
            totalcount += 1
print(count)
