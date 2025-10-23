a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

for x in a :
    if x<35: print(x)

print( [x for x in a if x<35] )