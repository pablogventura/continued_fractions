from fractions import Fraction as F

#https://en.wikipedia.org/wiki/Continued_fraction

def calculate(values):
    result = F(1/values.pop(-1))
    while len(values) > 1:
        a = values.pop(-1)
        result = F(1,result + a)
    result = values[0] + result
    return float(result)
    

golden=calculate([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

pi=calculate([3,7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2,2,2,2,1,84,
 2,1,1,15,3,13,1,4,2,6,6,99,1,2,2,6,3,5,1,1,6,8,1,
 7,1,2,3,7,1,2,1,1,12,1,1,1,3,1,1,8,1,1,2,1,6,1,1,
 5,2,2,3,1,2,4,4,16,1,161,45,1,22,1,2,2,1,4,1,2,24,
 1,2,1,3,1,2,1])

sqrt2 = calculate([1]+[2]*10)
