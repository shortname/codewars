identity = lambda x: x   

def zero(equation=identity): #your code here
    return equation(0)
def one(equation=identity): #your code here
    return equation(1)
def two(equation=identity): #your code here
    return equation(2)
def three(equation=identity): #your code here
    return equation(3)
def four(equation=identity): #your code here
    return equation(4)
def five(equation=identity): #your code here
    return equation(5)
def six(equation=identity): #your code here
    return equation(6)
def seven(equation=identity): #your code here
    return equation(7)
def eight(equation=identity): #your code here
    return equation(8)
def nine(equation=identity): #your code here
    return equation(9)

def plus(b):
    return lambda a: a + b
def minus(b): #your code here
    return lambda a: a - b
def times(b): #your code here
    return lambda a: a * b
def divided_by(b): #your code here
    return lambda a: a // b