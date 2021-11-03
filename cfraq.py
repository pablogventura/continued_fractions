from fractions import Fraction as F

#https://en.wikipedia.org/wiki/Continued_fraction

def calculate(values):
    result = F(1/values.pop(-1))
    while len(values) > 1:
        a = values.pop(-1)
        result = F(1,result + a)
        for a in values:
            result = F(result/a)
    result = values[0] + result
    return float(result)
    

golden=calculate([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
 
sqrt2 = calculate([1]+[2]*10)
