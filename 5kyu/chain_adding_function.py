class NumberChain(int):
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num):
        return self.num + num
        
    def __call__(self, num):
        return NumberChain(self.num + num)
        
    def __eq__(self, num):
        return self.num == num

add = NumberChain