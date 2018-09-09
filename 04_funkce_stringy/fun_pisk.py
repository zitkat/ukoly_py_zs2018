

def urci_kdo_vyhral(hra):

    if "xxx" in hra:
        return "x"
    elif "ooo" in hra:
        return "o"
    elif not("-" in hra):
        return "!"
    else:
        return "-"


def tahni(hra, cislo_policka, symbol):
    assert((0 <= cislo_policka) and (cislo_policka < len(hra)))
    return hra[0:cislo_policka] + symbol + hra[cislo_policka+1:]




if __name__ == '__main__':
    hra = input(">")
    print(tahni(hra, 1, "c"))

