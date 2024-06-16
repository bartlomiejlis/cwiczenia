# Napisz program proszacy uzytkownika o podanie dwóch liczb a i b i wypisujacy ich sume, róznice, iloczyn,
# iloraz, pierwiastek z a + b oraz a do potęgi b i b do potęgi a.

import math

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

print('Suma:', a + b)
print('Różnica:', a - b)
print('Iloczyn:', a * b)
print('Iloraz:', a / b)
print('Pierwiastek z a + b:', math.sqrt(a + b))
print('a do potęgi b:', a ** b)
print('b do potęgi a:', b ** a)
