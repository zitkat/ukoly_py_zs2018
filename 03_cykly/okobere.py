from random import randint
body = 0


while body <= 21:
    print("Máte {0} bodů, to je dobré".format(body))
    pokracovat = input("Prejete si pokracovat [ano]/ne? ")
    if pokracovat != "ne":
        body += randint(2, 10)
    else:
        break

if body > 21:
    print("Prohráli jste, smůla")
elif body == 21:
    print("Oko bere!")
else:
    print("Aspoň jste neprohráli.")
