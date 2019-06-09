import re

class FSM(object):
    def __init__(self, instructions):
        records = instructions.split('\n')
        pattern = re.compile(r'([^;]+); ([^,]+), ([^;]+); (\d+)')
        self._states = {m.group(1): {0: m.group(2), 1: m.group(3), 'value': int(m.group(4))} for m in map(pattern.search, records)}
    
    def run_fsm(self, start, sequence):
        state_name = start
        path = [start]
        for s in sequence:
            state_name = self._states[state_name][s]
            path.append(state_name)
        return state_name, self._states[state_name]['value'], path