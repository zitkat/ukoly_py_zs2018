from random import randrange


class Hra:

    def vypis_herni_pole(self):
        print("Tohle je abstraktni hra.")

    def tah_hrace(self):
        print("na nic si nehrajem ale muzete zadat svoje jmeno")
        self.jmeno_hrace = str(input("> "))

    def tah_pocitace(self):
        print("Ja jsem pocitac a ty jsi {}".format(self.jmeno_hrace))

    def vyhodnot(self):
        return ""


class Piskrovky1D(Hra):

    def __init__(self, velikost=20):
        self.velikost = velikost
        self.herni_pole = velikost*"-"

    def tahni(self, herni_pole, cislo_policka, symbol):
        """
        Zapíše symbol na pozici cislo_policka v řetězci hra,
        vrátí nový řetězec
        :param herni_pole:
        :param cislo_policka:
        :param symbol:
        :return:
        """
        return herni_pole[0:cislo_policka] + symbol + herni_pole[cislo_policka + 1:]

    def tah_hrace(self):
        """
        Ptá se hráče na tah dokud se nepodaří,
        zaznamená tah do herni_pole znakem x

        """
        # print("Stav hry je: ")
        # print(self)
        while True:
            pozice = int(input("Jak chcete hrat? "))
            if (0 < pozice) and (pozice <= self.velikost):
                if self.herni_pole[pozice - 1] == "-":
                    self.herni_pole = self.tahni(self.herni_pole, pozice - 1, "x")
                    return
                else:
                    print("Obsazena pozice, hrajte jinam.")
            else:
                print("Hrajte jen v herním poli, tj. od 1 do {}".format(self.velikost))

    def tah_pocitace(self):
        """
        Náhodně táhne "o" na volné pole v herni_pole
        """
        print("Hraje pocitac")
        while True:
            pozice = int(randrange(0, self.velikost))
            if self.herni_pole[pozice] == "-":
                self.herni_pole = self.tahni(self.herni_pole, pozice, "o")
                return

    def vyhodnot(self):
        """
        :param hra:
        :return: "x" při výhře x,
                 "o" při výhře o
                 "!" při remíze
                 "-" při otevřené hře
        """
        if "xxx" in self.herni_pole:
            return "hrac"
        elif "ooo" in self.herni_pole:
            return "pocitac"
        elif not ("-" in self.herni_pole):
            return "remiza"
        else:
            return ""

    def vypis_herni_pole(self):
        print("Stav hry je")
        print(self.herni_pole)


class Piskvorky2D(Hra):
    def __init__(self, velikost=5):
        self.velikost = velikost
        self.herni_pole = list()
        for i in range(velikost):
            self.herni_pole.append(list(20*"."))

    def vypis_herni_pole(self):
        for i in range(self.velikost):
            for j in range(self.velikost):
                print(self.herni_pole[i][j], end=" ")
            print()

    def tah_hrace(self):
        while True:
            print("Jak chcete hrat? ")
            sloupec = int(input("Sloupec> "))
            radek = int(input("Radek> "))

            if ((0 < sloupec) and (sloupec <= self.velikost) and
                (0 < radek) and (radek <= self.velikost)):
                if self.herni_pole[radek - 1][sloupec -1] == ".":
                    self.herni_pole[radek - 1][sloupec - 1] = "x"
                    return
                else:
                    print("Obsazena pozice, hrajte jinam.")
            else:
                print("Hrajte jen v herním poli, tj. od 1 do {}".format(self.velikost))

    def tah_pocitace(self):
        """
        Náhodně táhne "o" na volné pole v herni_pole
        """
        print("Hraje pocitac")
        while True:
            sloupec = int(randrange(0, self.velikost))
            radek = int(randrange(0, self.velikost))

            if self.herni_pole[sloupec][radek] == ".":
                self.herni_pole[sloupec][radek] = "o"
                return

    def vyhodnot(self):

        remiza = True
        for i in range(self.velikost):
            if "." in self.herni_pole[i]:
                remiza = False
        if remiza:
            return "remiza"

        def vyherce(znak):
            if znak == "o":
                return "pocitac"
            else:
                return "hrac"

        for i in range(self.velikost):
            for j in range(self.velikost):
                stred = self.herni_pole[i][j]
                if stred == ".":
                    continue
                if self.je_uvnitr(i+1, j) and self.je_uvnitr(i-1, j):
                    if (stred == self.herni_pole[i+1][j]) and (stred == self.herni_pole[i-1][j]):
                        return vyherce(stred)
                if self.je_uvnitr(i, j+1) and self.je_uvnitr(i, j-1):
                    if (stred == self.herni_pole[i][j+1]) and (stred == self.herni_pole[i][j-1]):
                        return vyherce(stred)
                if self.je_uvnitr(i+1, j+1) and self.je_uvnitr(i-1, j-1):
                    if (stred == self.herni_pole[i+1][j+1]) and (stred == self.herni_pole[i-1][j-1]):
                        return vyherce(stred)
                if self.je_uvnitr(i-1, j+1) and self.je_uvnitr(i+1, j-1):
                    if (stred == self.herni_pole[i-1][j+1]) and (stred == self.herni_pole[i+1][j-1]):
                        return vyherce(stred)

        return ""

    def je_uvnitr(self, sloupec, radek):

        return((0 <= sloupec) and (sloupec < self.velikost) and (0 <= radek) and (radek < self.velikost))


hry = {"piskvorky 1D": Piskrovky1D,
       "piskvorky 2D": Piskvorky2D}


def vyber_hru():
    print("Jakou hru si chcete zahrát? ")
    while True:
        vybrana_hra = str(input("Na výběr máte: {}\n> ".format(list(hry.keys()))))
        if vybrana_hra in hry:
            return hry[vybrana_hra]
        else:
            print("Tuhle hru neznám :(")


def hrej_hru(hra):
    hra.vypis_herni_pole()
    while True:
        hra.tah_hrace()
        hra.vypis_herni_pole()
        if hra.vyhodnot() != "":
            break
        hra.tah_pocitace()
        hra.vypis_herni_pole()
        if hra.vyhodnot() != "":
            break

    if hra.vyhodnot() == "remiza":
        print("Remíza, nikdo nevyhrál.")
    elif hra.vyhodnot() == "hrac":
        print("Gratuluji vyhráli jste.")
    else:
        print("Ted jsem vyhrál já.")


if __name__ == '__main__':
    while True:
        hrat_dal = str(input("Chcete si zahrát hru? "))
        if "ne" in hrat_dal.lower():
            print("Mejte se!")
            break
        typ_hry = vyber_hru()
        hra = typ_hry()
        hrej_hru(hra)

