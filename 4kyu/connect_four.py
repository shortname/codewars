from collections import defaultdict
import re
from functools import reduce
import operator

COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY = ' '

def find_winners_in_lists(state_arr):
    return reduce(operator.concat, [re.findall(r'([A-Z][a-z]+)\1\1\1', col) for col in map(lambda c: ''.join(c), state_arr) if len(col) > 0], [])

def find_winners(state):
    state_arr = [[state[c][i] if len(state[c]) > i else EMPTY for i in range(6)] for c in COLUMNS]
    columns = find_winners_in_lists(state_arr)
    transposed = list(zip(*state_arr))
    rows = find_winners_in_lists(transposed)
    diagonals = find_winners_in_lists(zip(*[list(transposed[i][i:7])+[EMPTY]*(7-i) for i in range(len(transposed))]))
    diagonals2 = find_winners_in_lists(zip(*[[EMPTY]*i + list(transposed[i][0:7-i]) for i in range(len(transposed))]))
    combined = set(columns + rows + diagonals + diagonals2)
    return combined

def who_is_winner(psl):
    state = defaultdict(list)
    for p in psl:
        col, pl = p.split('_')
        state[col].append(pl)
        combined = find_winners(state)
        if len(combined) == 1:
            return combined.pop()
        elif len(combined) == 2:
            return 'Draw'
    return 'Draw'  