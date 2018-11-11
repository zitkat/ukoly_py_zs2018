tah_cloveka = input("Kámen, nůžky nebo papír?: ")
tah_pocitace = "kámen"

if tah_cloveka == tah_pocitace:
    print("Plichta")
elif tah_cloveka == "kámen":
    if tah_pocitace == "nůžky":
        print("Vyhhrali jste.")
    elif tah_pocitace == "papír":
        print("Vyhrál jsem.")
elif tah_cloveka == "nůžky":
    if tah_pocitace == "kámen":
        print("Vyhrál jsem.")
    elif tah_pocitace == "papír":
        print("Vyhrali jste.")
elif tah_cloveka == "papír":
    if tah_pocitace == "nůžky":
        print("Vyhrál jsem.")
    elif tah_pocitace == "kámen":
        print("Vyhrali jste.")
else:
    print("Takhle se to nehraje")
