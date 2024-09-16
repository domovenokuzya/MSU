from math import sqrt

def BiquadEq (a, b, c):
    res = []
    if a == 0:
        if b == 0:
            if c == 0:
                res.append(-1)
            else:
                res.append(0)
            return res
        elif -c/b <= 0:
            res.append(0)
            return res
        else:
            res.append(-sqrt(-c/b))
            res.append(sqrt(-c/b))
            return res
    else:
        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            res.append(0)
            return res
        elif discriminant == 0:
            if -b / (2 * a) <= 0:
                res.append(0)
                return res
            else: 
                res.append(-sqrt(-b/(2*a)))
                res.append(sqrt(-b/(2*a)))
                return res
        else:
            y_1 = (-b + sqrt(discriminant)) / (2 * a)
            y_2 = (-b - sqrt(discriminant)) / (2 * a)
            if y_1 == 0:
                res.append(0)
            elif y_1 > 0:
                res.append(-sqrt(y_1))
                res.append(sqrt(y_1))
            if y_2 == 0:
                res.append(0)
            elif y_2 > 0:
                res.append(-sqrt(y_2))
                res.append(sqrt(y_2))
            if len(res) == 0:
                res.append(0)
                return res
            res.sort()
            return res



coefficients = map(int, input().split(','))
a, b, c = coefficients
print(' '.join(map(str, BiquadEq(a, b, c))))
