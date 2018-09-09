import turtle as t


def nakresli_dum(strana):
    """
    Tahle nakresli domecek jednim tahem,
    jde to ale spousty jinych zpusobu,
    

    :param strana je vyska steny domku
    """
    # nejdriv ctverec
    from math import sqrt
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)
    t.forward(strana)
    t.left(90)

    # diagonala z leveho dolniho rohu do praveho horniho
    t.left(45)
    t.forward(sqrt(2) * strana)

    # strecha je taky diagonala ale kreslime z ni jen pulku
    t.left(90)
    t.forward(sqrt(2) * strana / 2)
    t.left(90)
    t.forward(sqrt(2) * strana / 2)

    # a do praveho dolniho rohu
    t.left(90)
    t.forward(sqrt(2) * strana)
    t.left(45)


if __name__ == '__main__':
    nakresli_dum(10)
    t.forward(20)
    nakresli_dum(20)
    t.forward(30)
    nakresli_dum(50)
