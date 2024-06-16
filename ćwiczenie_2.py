# Napisz program proszacy uzytkownika o imie i rok urodzenia, a nastepnie obliczajacy i wypisujacy jego wiek.

name = input('Podaj swoje imię: ')
birth_year = int(input('Podaj rok urodzenia: '))
current_year = 2024
age = current_year - birth_year

print(f'{name}, masz {age} lat.')
