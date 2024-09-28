def get_matrix(n=4, m=2, value=13):
    matrix = []

    for i in range(0, n):
        r1 = []
        matrix.append(r1)
        for j in range(0, m):
            r2 = [value]
            r1.append(*(r2))

    print(matrix)
get_matrix()


