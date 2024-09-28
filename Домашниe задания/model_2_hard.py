N = 3
password = str()
for i in range(1,N//2+1):
    for j in range(i+1, N):
        i_j = i+j
        if N % i_j == 0:
            password += f'{i}{j}'

print(f'{password}')
