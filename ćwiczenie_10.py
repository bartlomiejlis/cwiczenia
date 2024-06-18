# Napisz funkcje, która dla dowolnej sekwencji podanej jako argument, obliczy ile razy wystapił w niej kazdy
# z elementów i zwróci te dane jako wynik. Nastepnie wypisz liczbe wystapien kazdego elementu na ekran
# zaczynajac od elementu najmniejszego. Niezbedne sortowanie powinno sie odbyc juz poza funkcja.
# W funkcji utwórz słownik, w którym kluczami sa poszczególne elementy sekwencji, a wartosciami - liczba ich wystapien.
# Do sortowania mozna uzyc wbudowanej funkcji sorted.
# Np. dla napisu "abzkfhiohfnlaanfnffnkkdamd" na ekran powinno sie wypisac:
# a : 4
# b : 1
# d : 2
# f : 5
# h : 2
# i : 1
# k : 3
# l : 1
# m : 1
# n : 4
# o : 1
# z : 1

def elements_counter(sequence):
    counter = {}
    for element in sequence:
        if element in counter.keys():
            counter[element] += 1
        else:
            counter.update({element: 1})
    return counter


counted_elements = elements_counter('abzkfhiohfnlaanfnffnkkdamd')
print(counted_elements)
counted_elements_sorted = sorted(counted_elements.items())
print(counted_elements_sorted)

for item in counted_elements_sorted:
    key = item[0]
    value = item[1]
    print(f'{key} : {value}')
