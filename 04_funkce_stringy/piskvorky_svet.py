__author__ = "Svetlana Spiglazova"

from random import randrange


def najdi_pozice(pole, hledany):
    seznam = []
    for cislo, znak in enumerate(pole):
        if znak == hledany:
            seznam.append(cislo)
    return seznam


def vyhodnot(pole):
    if 'xxx' in pole:
        print(pole)
        return 'x'
    elif 'ooo' in pole:
        print(pole)
        return 'o'
    elif '-' not in pole:
        print(pole)
        return '!'
    else:
        return '-'


def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici"
    :param pole:
    :param cislo_policka:
    :param symbol:
    :return:
    """
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole):
    cislo_policka = 0
    while True:
        print('zadej cislo policky')
        cislo_policka = int(input())
        if (cislo_policka >= 0) and (cislo_policka <= 19) and (pole[cislo_policka] == '-'):
            return tah(pole, cislo_policka, 'x')
        else:
            print('bud pole je obsazeno nebo cislo je zaporne nebo prilis velke')


def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    seznam = najdi_pozice(pole, 'x')
    for cislo_policka in seznam:
        if (cislo_policka == 0) and (pole[cislo_policka + 1] == '-'):
            return tah(pole, cislo_policka + 1, 'o')
        elif (cislo_policka == 19) and (pole[cislo_policka - 1] == '-'):
            return tah(pole, cislo_policka - 1, 'o')
        elif (cislo_policka > 0) and (cislo_policka < 19):
            if (pole[cislo_policka + 1] == '-'):
                return tah(pole, cislo_policka + 1, 'o')
            elif (pole[cislo_policka - 1] == '-'):
                return tah(pole, cislo_policka - 1, 'o')

    while True:
        cislo_policka = randrange(20)
        if '-' in pole[cislo_policka]:
            return tah(pole, cislo_policka, 'o')


def piskvorky1d():
    pole = '-' * 20
    while '-' in pole:
        print(pole)
        pole = tah_hrace(pole)
        pole = tah_pocitace(pole)
        result = vyhodnot(pole)
        if result != '-':
            print(result)
            break


def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka).lower().strip()
        if (odpoved == 'ano') or (odpoved == 'a'):
            return True
        elif (odpoved == 'ne') or (odpoved == 'n'):
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


if ano_nebo_ne('Chceš si zahrát hru? '):
    print(' Zaciname piskvorky ')
    piskvorky1d()
else:
    print('Škoda.')