STRIKE = 'X'
SPARE = '/'

class Frame:
    def __init__(self, symbol, next_frame):
        self.symbol = symbol
        self.values = [int(s) if s.isdigit() else 10 for s in self.symbol]
        if SPARE in self.symbol:
            spare_index = self.symbol.find(SPARE)
            self.values[spare_index] = 10 - self.values[spare_index - 1]
        self.length = len(self.values)
        self.next_frame = next_frame

    def value(self):
        return sum(self.values) + self.bonus() + (self.next_frame.value() if self.next_frame else 0)

    def bonus(self):
        if self.next_frame:
            if STRIKE in self.symbol:
                result = self.next_frame.values[0]
                if self.next_frame.length > 1:
                    return result + self.next_frame.values[1]
                elif self.next_frame.next_frame:
                    return result + self.next_frame.next_frame.values[0]
                else:
                    return result
        if SPARE in self.symbol and self.next_frame:
            return self.next_frame.values[0]
        return 0


def bowling_score(frames):
    frames_list = frames.split(' ')
    frames_chain = None
    for f in frames_list[::-1]:
        frames_chain = Frame(f, frames_chain)
    return frames_chain.value()