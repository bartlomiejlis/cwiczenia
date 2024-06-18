# Napisz program, który:
# - utworzy pusta liste i wypełni ja piecioma liczbami losowymi z dowolnego zakresu, np. [−1, 1]
# (do generowania liczb mozesz uzyc np. funkcji uniform z modułu random, której wywołanie uniform(a,b)
# zwraca liczbe z przedziału [a, b]);
# - wypisze po kolei wszystkie elementy listy wraz z indeksami w nastepujacy sposób:
# lista [0]: 0.1
# lista [1]: -0.92
# itd.
# - wypisze długosc listy, czyli ilosc jej elementów;
# - znajdzie i wypisze najwiekszy element listy oraz jego indeks.

import random

my_list = []

for _ in range(5):
    my_list.append(random.uniform(-1, 1))

for num in my_list:
    index = my_list.index(num)
    print(f'lista [{index}]: {num}')

my_list_len = len(my_list)
print(f'\nLista zawiera {my_list_len} elementów.')

max_element = max(my_list)
max_element_index = my_list.index(max_element)
print(f'\nZnaleziono największy elemeny {max_element}, o indeksie [{max_element_index}].')
