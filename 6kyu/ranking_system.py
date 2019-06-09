def rankings(arr):
    place = 1
    length = len(arr)
    result = [0]*length
    while max(arr) > 0:
        maxval = max(arr)
        found = False
        for i in range(0, length):
            if arr[i] == maxval:
                result[i] = place
                arr[i] = 0
                found = True
        if found:
            place += 1
    return result