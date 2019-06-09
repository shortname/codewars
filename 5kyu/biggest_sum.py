def find_sum(m):
    M = len(m)
    r = [[0 for _ in range(M)] for _ in range(M)]
    for x in range(0, M):
        for y in range(0, M):
            r[x][y] = m[y][x]
            options = [0]
            if x > 0:
                options.append(r[x-1][y])
            if y > 0:
                options.append(r[x][y-1])
            r[x][y] += max(options)
    return r[M-1][M-1]