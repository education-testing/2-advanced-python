# Crud en la estructura de dato set
set_country = {"col", "mex", "bol"}
print(len(set_country))

print("col" in set_country)  # saber si col, está en la estructura
print("per" in set_country)
print("mex" in set_country)

print("ADD")
set_country.add("per")
print("-------- peru")
print("mex" in set_country)
print("per" in set_country)
print(set_country)

print("UPDATE")
set_country.update({'arg', 'ecu', 'per'})
print(set_country)

print("REMOVE")
set_country.remove("per")
print(set_country)

print("DISCARD")  # Esto remueve igualmente, pero valida, si el elemento no existe, no lanza error, es más amigable.
set_country.discard("pe")  # Esto no existe.
print(set_country)

print("CLEAR")
set_country.clear()
print(len(set_country))
