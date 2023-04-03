from operators import *

def calc(a, b, oper):
    if oper == '+':
        result = summa(float(a), float(b))
    elif oper == '-':
        result = minus(float(a), float(b))
    elif oper == '*':
        result = mult(float(a), float(b))
    elif oper == '/':
        result = div(float(a), float(b))
    return result