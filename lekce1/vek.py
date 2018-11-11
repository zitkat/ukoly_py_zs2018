vek = int(input("Zadej vek: "))

if vek > 120:
    print("Jsi ze Země?")
elif vek > 50:
    print("Mas slevu na jizdné")
elif vek < 18:
    print("Tobe nenaleju")
else:
    print("Zadnou slevu nedostanes")
