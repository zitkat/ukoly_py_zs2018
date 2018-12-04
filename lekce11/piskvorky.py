



while True:
    herni_pole = tah_hrace()
    if vyhodnot(herni_pole) != "hrajeme dal":
        break
    herni_pole = tah_pocitace()
    if vyhodnot(herni_pole) != "hrajeme dal":
        break

if vyhodnot(herni_pole) == "remiza":
    print("Remiza")
elif vyhodnot(herni_pole) == "pocitac":
    print("Vyhral jsem, cha cha!")
else:
    print("Vyhrali jste :(")