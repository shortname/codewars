def matrix_mult(a, b):
    M = len(a)
    return [[sum([a[y][i] * b[i][x] for i in range(M)]) for x in range(M)] for y in range(M)]