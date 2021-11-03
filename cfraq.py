from fractions import Fraction as F

def calculate(values):
    result = 1
    for a in values:
        result = F(result/a)
