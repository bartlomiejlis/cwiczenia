# Napisz funkcje, która przyjmuje wartosc temperatury w Kelvinach i zwraca wartosc wyrazona w stopniach
# Celsjusza: TC = TK − 272.15. W przypadku podania wartosci ujemnej funkcja zwraca None. Przetestuj jej
# działanie.

def temperature_conversion(kelvin_temperature: float) -> float | None:
    """Przyjmuje wartosc temperatury w Kelvinach i zwraca wartosc wyrazona w stopniach Celsjusza: TC = TK − 272.15.
    W przypadku podania wartosci ujemnej funkcja zwraca None.
    """
    if kelvin_temperature >= 0:
        celsius_temperature = kelvin_temperature - 272.15
        return print(celsius_temperature)
    return None


temperature_conversion(36.6)
temperature_conversion(-36.6)
