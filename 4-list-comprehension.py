print("1. Forma normal de hacer un lista con iteración")

# Declaro la lista
numbers = []

for element in range(1, 11):  # Itero de 1 a 10
    numbers.append(element)  # Agrego los elementos a lista

print(numbers)  # Imprimo la lista.

print("2. Forma de hacerlo con list-comprehension: ")

numbers_v2 = [element_1 for element_1 in range(1, 11)]
print(numbers_v2)

print("3. si necesito hacer validaciones dentro de los for: ")

numbers_v3 = [element_2 * 2 for element_2 in range(1, 101) if element_2 % 2 == 0]
print(numbers_v3)

print("4. una validación dentro de un for seria asi: ")
numbers_4 = []

for element_4 in range(1, 11):  # Itero de 1 a 10
    if element_4 % 2 == 0:
        numbers_4.append(element_4 * 2)  # Agrego los elementos a lista

print(numbers_4)  # Imprimo la lista.
