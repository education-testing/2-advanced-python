print("1. Versión normal de un diccionario: ")
dic = {}

for i in range(1, 5):
    dic[i] = i * 2

print(dic)

print("2. con dictionary-comprehension: ")

dic_v2 = {i: (i * 2) for i in range(1, 5)}
print(dic_v2)


print("3. Ejemplo con países: ")

import random
countries = ['col', 'per', 'mex', 'bol', 'arg']
dic_countries = {}

for i in countries:
    dic_countries[i] = random.randint(1, 100)

print(dic_countries)

print("4. ejemplo con dictionary-comprenhension: ")
countries = ['col', 'per', 'mex', 'bol', 'arg']

dic_countries_v2 = {i: random.randint(1, 100) for i in countries}
print(dic_countries_v2)

print("5. Revisión del método zip()")
names = ['alex', 'diana', 'carlos']
ages = [18, 19, 29]

x_dic = dict(zip(names, ages))
print(x_dic)

