# Napisz funkcje, która dla zadanego argumentu (którym moze byc lista, krotka lub inna sekwencja) zwraca
# indeks i wartosc najmniejszego elementu oraz indeks i wartosc najwiekszego elementu. Nastepnie, uzywajac
# składni list comprehension utwórz kilkunastoelementowa liste wypełniona losowymi liczbami całkowitymi i
# przetestuj na niej swoja funkcje.
# Uwaga. Python posiada wbudowane funkcje min, max itp. do znalezienia maksimum, minimum oraz indeksów.
# Mozna (ale nie jest to obowiazkowe) ich uzyc zeby sprawdzic, czy napisana przez nas funkcja daje
# poprawne wyniki. Jednak w funkcji nie nalezy ich uzywac - nalezy przejsc wszystkie elementy listy petla
# for, porównywac z czym trzeba i w ten sposób znalezc szukane wartosci.

import random


def min_max_sorter(sequence):
    sequence = list(sequence)
    sequence.sort()
    min_element = sequence[0]
    min_element_index = sequence.index(min_element)
    max_element = sequence[-1]
    max_element_index = sequence.index(max_element)
    return print(f'Najmniejsza wartość listy to {min_element} o indeksie [{min_element_index}].'
                 f'\nNajwiększa wartość listy to {max_element} o indeksie [{max_element_index}].')


random_numbers = [random.randint(1, 100) for _ in range(15)]
min_max_sorter(random_numbers)
