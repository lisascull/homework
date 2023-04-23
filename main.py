from math import *
def dovg (a1, b1, a2, b2) :
    dv = sqrt((a1 - a2)*(a1 - a2) + (b1 -b2)*(b1 - b2))
    return dv

print('vvedit koordunatu 1 tochku')
x1 = input()
y1 = input()
print('vvedit koordunatu 2 tochku')
x2 = input()
y2 = input()
print('vvedit koordunatu 3 tochku')
x3 = input()
y3 = input()

a = float(input('vvedit koordunatu 1 tochku'))
b = float(input('vvedit koordunatu 2 tochku'))
c = float(input('vvedit koordunatu 3 tochku'))

p = (a+b+c)/2.0
S = sqrt(p*(p - a)*(p - b)*(p - c))

print('plosha triangle', S)

