from math import *

a = float(input('vvedit koordunatu 1 tochku'))
b = float(input('vvedit koordunatu 2 tochku'))
c = float(input('vvedit koordunatu 3 tochku'))

p = (a+b+c)/2.0
S = (p*(p - a)*(p - b)*(p - c))

print('plosha triangle', S)

