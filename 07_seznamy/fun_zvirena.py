

domaci_zvirata = ["kráva", "pes", "kocka", "králík", "had", "andulka"]


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


def je_v_seznamu(slovo, seznam=domaci_zvirata):
    return slovo in seznam


def serad_abecedne(seznam):
    return sorted(seznam)


print(serad_abecedne(domaci_zvirata))


