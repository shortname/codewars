import inspect

def log(f):
    def fl(*args):
        print(f.__name__, *args)
        return f(*args)
    return fl

class DegreeCounter:
    def __init__(self, degree=1, factor=1, state=None):
        self.degree = degree
        self.factor = factor
        self.state = state
        
    @log
    def __mul__(self, num):
        if isinstance(num, DegreeCounter):
            return DegreeCounter(self.degree + num.degree, self.factor * num.factor)
        return DegreeCounter(self.degree, self.factor*num)
    
    @log
    def __add__(self, num):
        if not self.state: 
            self.state = {
                self.degree: self.factor
            }
        if isinstance(num, DegreeCounter):
            if self.state.get(num.degree):
                self.state[num.degree] += num.factor
            else:
                self.state[num.degree] = num.factor   
        return self
    
    @log
    def __sub__(self, num):
        if not self.state:
            self.state = {
                self.degree: self.factor
            }
        if isinstance(num, DegreeCounter):
            if self.state.get(num.degree):
                self.state[num.degree] -= num.factor
            else:
                self.state[num.degree] = -num.factor   
        return self
    
    @log
    def __rsub__(self, num):
        if not self.state:
            self.state = {
                self.degree: -self.factor
            } 
        if not isinstance(num, DegreeCounter):
            self.state[self.degree] = -self.state[self.degree]   
        return self
    
    @log
    def __pow__(self, num):
        return DegreeCounter(self.degree * num)
    
    @log
    def __neg__(self):
        self.factor = -self.factor
        return self
    
    @log
    def __truediv__(self, num):
        if isinstance(num, DegreeCounter):
            return DegreeCounter(self.degree - num.degree, self.factor / num.factor)
        return self
    
    @log
    def __rtruediv__(self, num):
        if isinstance(num, DegreeCounter):
            return DegreeCounter(num.degree - self.degree, num.factor / self.factor)
        return self
    
    def __repr__(self):
        return '(DC; d: {}; f: {}; s: {})'.format(self.degree, self.factor, self.state)

DegreeCounter.__radd__ = DegreeCounter.__add__
DegreeCounter.__rmul__ = DegreeCounter.__mul__

def degree(p):
    dc = p(DegreeCounter())
    if isinstance(dc, DegreeCounter):
        if dc.state:
            relevant = [s[0] for s in dc.state.items() if s[1] != 0]
            print(dc.state)
            return max(relevant) if len(relevant) > 0 else 0
        else:
            return dc.degree if dc.factor != 0 else 0
    return 0