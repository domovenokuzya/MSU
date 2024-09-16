from math import sqrt

def isPower(n):
    nn = int(sqrt(n)) + 1
    for i in range(2, nn):
        x = float(n)
        while x != 1 and x.is_integer():
            x = x / i
            if x == 1:
                return "YES"
    return "NO"

    

n = int(input())
print(isPower(n))