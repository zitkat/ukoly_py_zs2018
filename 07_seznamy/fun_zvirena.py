

domaci_zvirata = ["kráva", "pes", "kočka", "králík", "had", "andulka"]
dom_zvirata = ["pes", "kočka", "králík", "had"]


def vytvor_listy(seznam1, seznam2):

    s1ms2 = []
    s2ms1 = []
    s1Us2 = []

    for polozka in seznam1 + seznam2:
        if polozka not in seznam2:
            s1ms2.append(polozka)
        if polozka not in seznam1:
            s2ms1.append(polozka)
        if polozka not in s1Us2:
            s1Us2.append(polozka)
    return s1Us2, s1ms2, s2ms1



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
print(vytvor_listy(dom_zvirata, domaci_zvirata))


