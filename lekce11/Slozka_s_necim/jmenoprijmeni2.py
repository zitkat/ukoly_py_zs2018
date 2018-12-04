jmeno_prijmeni = input("Ahoj. Jak se jmenuješ? Cele jmeno prosim.")

ova = "ova"
jmeno, prijmeni = jmeno_prijmeni.split()
print ("Ahoj" , jmeno)

if ("ova" in prijmeni) == True:
	print ("Jsi holka?")
else:
	print ("Jsi kluk")

