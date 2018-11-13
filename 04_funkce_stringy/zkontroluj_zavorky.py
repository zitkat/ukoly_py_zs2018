def zavorky_ok(retezec):
    otevreno = 0
    for c in retezec:
        if c == "(":
            otevreno += 1
        elif c == ")":
            otevreno -= 1
            if otevreno < 0:
                return False
    return otevreno == 0


retezec = str(input("Zadejte retezec, jehoz zavorky, chete zkontrolovat \n: "))
# retezec = "(()()(()))"
print(zavorky_ok(retezec))
