strana = float(input("Zadejte stranu čtverce: ")) # nacte cislo od uzivatele
spravna_strana = strana > 0
if spravna_strana == True:
    print("Obsah čtverce o straně", strana, "cm je ", strana**2, "cm2")
    print("Obvod čtverce o straně", strana, "cm je ", 4*strana, "cm")
else:
    print("Zadali jste spatnou stranu.")
