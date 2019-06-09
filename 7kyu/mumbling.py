def accum(s):
    return '-'.join([s[i].upper() + s[i].lower()*i for i in range(0, len(s))])