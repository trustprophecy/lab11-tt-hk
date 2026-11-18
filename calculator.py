"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return b / a
def logarithm(a, b=math.e): 
    if a <= 0:
        raise ValueError("number must be greater than zero and positive")
    if b <= 0 or b == 1:
        raise ValueError("base must be postive and cannot equal one")
    return math.log(a, b)

def exponent(a,b):
    a ** b

