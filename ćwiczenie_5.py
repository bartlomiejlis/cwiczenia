# Napisz program, który wylosuje dowolna liczbe całkowita od zera do 10 (do losowania liczb uzyj np. funkcji
# randint z biblioteki random), a nastepnie prosi uzytkownika o jej zgadniecie tak długo, az ten poda poprawna wartosc.
# Gdy program działa, rozszerz go np. o podawanie informacji za którym razem udało sie zgadnac lub o wskazówki typu
# ”Podana przez ciebie liczba jest wieksza/mniejsza od wylosowanej”.

import random

drawn_number = random.randint(0, 10)
guessed_number = int(input('Odgadnij liczbę z zakresu od 0 do 10: '))
tries = 0

while guessed_number != drawn_number:
    if guessed_number > drawn_number:
        print('Podana przez ciebie liczba jest większa od wylosowanej.')
    else:
        print('Podana przez ciebie liczba jest mniejsza od wylosowanej.')
    guessed_number = int(input('Spróbuj ponownie: '))
    tries += 1

print(f'Zgadłeś za {tries} razem.')
