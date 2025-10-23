numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11];
menosFnums = [];
menosNnums = [];

for num in numbers:
    if num < 10 :
        menosFnums.append(num);
        menosFnums.sort();
print(menosFnums);
print();

num = int(input("Digite seu número: "));
for n in numbers :
    if n < num :
        menosNnums.append(n);
        menosNnums.sort();
print(menosNnums);
print();