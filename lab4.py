import math

def pole_kola(promien):
    """ Oblicza pole koła o danym promieniu."""
    pole = math.pi * promien**2
    print(f"Pole koła o promieniu {promien} wynosi: {pole}")

def pole_trapezu(a, b, h):
    """Oblicza pole trapezu o podanych wymiarach."""
    pole = 0.5 * (a + b) * h
    print(f"Pole trapezu o podstawach {a} i {b} oraz wysokości {h} wynosi: {pole}")


def wypisz_imie_wiek(imie, wiek=20):
    """Wypisuje na ekranie podane imię i wiek."""
    print(f"Imię: {imie}, Wiek: {wiek}")
pole_trapezu(3, 7, 4)
pole_kola(4)
wypisz_imie_wiek("Jan", 25)
wypisz_imie_wiek("Anna")
print(pole_kola.__doc__)
print(pole_trapezu.__doc__)
print(wypisz_imie_wiek.__doc__)