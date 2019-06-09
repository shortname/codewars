import re

def scramble(s1, s2):
    if len(s1) < len(s2):
        return False
    s = ''.join([l for l in s1 if l in s2])
    if len(s) < len(s2):
        return False
    while len(s) > 0 and len(s2) > 0:
        l = str(s2[0])
        s, n = re.subn(l, '', str(s))
        s2, n2 = re.subn(l, '', str(s2))
        if n < n2 or len(s) < len(s2):
            return False
    return True