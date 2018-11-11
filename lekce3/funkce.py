from math import pi

def pozdrav(jmeno):
    print("Ahoj", jmeno, "!")

# pozdrav("pyLadies")
# pozdrav("Filipe")
# pozdrav("Magdo")

def ano_nebo_ne(otazka):
    anone = input(otazka)
    if anone == "ano":
        print("Odpověď zní ano")
        #return True
    elif anone == "ne":
        print("Opodvěď zní ne.")
        #return False
    else:
        print("Neplatná odpověď")

# odpoved = ano_nebo_ne("Máš mě rád? ")
# print(odpoved)

def spocti_obsah_elipsy(a, b):
    obsah = a * b * pi
    return obsah

def spocti_objem_valce(a, b, vyska):
    objem = spocti_obsah_elipsy(a, b) * vyska
    return objem


r1 = float(input("zadejte 1. osu "))
r2 = float(input("zadejte 2. osu "))
v
print(spocti_obsah_elipsy(r1, r2))
