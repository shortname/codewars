import re, math

FILLER = '\x0b'
SPLITTER = '\n'

def code(s):
    n = math.ceil(math.sqrt(len(s)))
    sn = s + FILLER*(n**2-len(s))
    splitted = [sn[k*n:k*n+n] for k in range(n)]
    rotated = [''.join(w) for w in zip(*reversed(splitted))]
    return SPLITTER.join(rotated)

def decode(s):
    splitted = s.split(SPLITTER)
    rotated = reversed([''.join(w) for w in zip(*splitted)])
    joined = ''.join(rotated)
    return re.sub(FILLER, '', joined)