# Utwórz dwa zbiory i wypełnij je kilkoma losowymi liczbami całkowitymi z dowolnego przedziału, np. od
# 1 do 10 (przedział nie powinien byc zbyt szeroki, zeby zbiory mogły miec jakas czesc wspólna). Nastepnie
# wypisz ich: sume, róznice i czesc wspólna, a takze te elementy, które pojawiaja sie tylko w jednym z nich.

import random

set_1 = set()
set_2 = set()

for _ in range(10):
    set_1.add(random.randint(1, 10))
    set_2.add(random.randint(1, 10))

print('Zbiór 1:', set_1)
print('Zbiór 2:', set_2)
print('\nSuma obu zbiorów to:', set_1.union(set_2))
print('Różnica zbiorów to:', set_1.difference(set_2))
print('Część wspólna zbiorów to:', set_1.intersection(set_2))
print('Indywidualne elementy zbiorów to:', set_1.symmetric_difference(set_2))
