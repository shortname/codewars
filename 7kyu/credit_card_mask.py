# return masked string
def maskify(cc):
    l=len(cc)
    t=4
    s=l-t if l - t > 0 else 0
    return '#' * s + cc[s:l]