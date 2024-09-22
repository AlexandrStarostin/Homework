numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(f'numbers:      {numbers}')
print(*[])

pri = []
not_pri = []

for i in numbers:
    if i != True:
        not_pri.append(i)
        numbers.remove(i)

print(f'not_primes:   {not_pri}')
print(*[])


for i in numbers:
    if  i != True:
        pri.append(i)

print(f'primes:       {pri}')




