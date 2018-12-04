from random import randint


def vymen(herni_pole, pozice, znak):

    pole_s_vymenou = herni_pole[:pozice] + znak + herni_pole[pozice + 1:]

    return pole_s_vymenou


def tah_hrace(herni_pole):

    while True:
        pozice = int(input("Zadejte svuj tah od 1 do 20> ")) -1
        if (0 <= pozice) and (pozice <= 19):
            if herni_pole[pozice] == "-":
                nove_herni_pole = vymen(herni_pole, pozice, "x")
                break
            else:
                print("Obsazena pozice, zadejte neco jineho.")
        else:
            print("Zadejte pozici od 1 do 20.")

    return nove_herni_pole

def tah_pocitace(herni_pole):

    while True:
        pozice = randint(0, 19)
        if herni_pole[pozice] == "-":
            nove_herni_pole = vymen(herni_pole, pozice, "o")
            break

    return nove_herni_pole

def vyhodnot(herni_pole):
    if "ooo" in herni_pole:
        return "pocitac"
    if "xxx" in herni_pole:
        return "hrac"
    if "-" not in herni_pole:
        return "remiza"


    return "hrajeme dal"


herni_pole = 20*"-"
while True:
    herni_pole = tah_hrace(herni_pole)
    if vyhodnot(herni_pole) != "hrajeme dal":
        break
    print(herni_pole)

    herni_pole = tah_pocitace(herni_pole)
    if vyhodnot(herni_pole) != "hrajeme dal":
        break
    print(herni_pole)

if vyhodnot(herni_pole) == "remiza":
    print("Remiza")
elif vyhodnot(herni_pole) == "pocitac":
    print("Vyhral jsem, cha cha!")
else:
    print("Vyhrali jste :(")