# Napisz program, który prosi o podanie liczby naturalnej, a nastepnie wypisuje z ilu cyfr składa sie wpisana
# wartosc, a takze informacje o sumie tworzacych ja cyfr. Dla uproszczenia załóz, ze podana liczba jest
# poprawna (czyli rzeczywiscie naturalna).

num = str(input('Podaj liczbę naturalną: '))
num_len = len(num)
print(f'Podana liczba naturalna składa się z {num_len} cyfr.')

total = 0
for i in num:
    total += int(i)

print('Suma cyfr tworzących liczbę naturalną to:', total)
