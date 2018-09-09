

domaci_zvirata = ["pes", "kocka", "králík", "had"]


def vrat_kratsi5(seznam):
    res = []
    for e in seznam:
        if len(e) < 5:
            res.append(e)
    return res


def vrat_k(seznam):
    res = []
    for e in seznam:
        if e[0].lower() == "k":
            res.append(e)
    return res


def je_seznamu(slovo, seznam=domaci_zvirata):
    return slovo in seznam

