# Napisz program, który oblicza pole i obwód koła o promieniu podanym przez uzytkownika. Wartosc stałej
# pi wez z biblioteki math. Promien nie moze byc ujemny. W przypadku podania liczby ujemnej, program
# powinien wypisywac komunikat informujacy o błednej wartosci i nic nie liczyc.

from math import pi

r = int(input('Podaj wartość promienia: '))

if r >= 0:
    circle_area = pi * r ** 2
    print('Powierzchnia koła wynosi:', circle_area)

    circle_circumference = 2 * pi * r
    print('Obwód koła wynosi:', circle_circumference)
else:
    print('Promień nie może być ujemny.')
