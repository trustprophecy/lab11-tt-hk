# [https://github.com/trustprophecy/lab11-tt-hk](https://github.com/trustprophecy/lab11-tt-hk)
# Partner 1: Trust Thomas
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("number must be greater than zero and positive")
        return math.sqrt(a)
    except ValueError as e:
        print (f"Error: {e}")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b
def logarithm(a, b=math.e): 
    if a <= 0:
        raise ValueError("number must be greater than zero and positive")
    if b <= 0 or b == 1:
        raise ValueError("base must be postive and cannot equal one")
    return math.log(a, b)
def exp(a,b):
    return a ** b

