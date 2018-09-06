a = float(input("Zadejte číslo a> "))
b = float(input("Zadejte číslo b> "))
op = input("Zadejte operaci> ")

if op == "+":
    vys = a+b
elif op == "-":
    vys = a - b
elif op == "/":
    vys = a / b
else:
    vys = "nevim"

print("a", op, "b je", vys)





# dale je priklad dost pokrocile konstrukce,
# koukni se na nej az na konci kurzu,
# az toho budes umet vic
ops = {"+": lambda x, y: x + y,
       "-": lambda x, y: x - y,
       "*": lambda x, y: x * y,
       "/": lambda x, y: x / y}

print("a", op, "b je", ops[op](a, b) if op in ops else "Nevim")
