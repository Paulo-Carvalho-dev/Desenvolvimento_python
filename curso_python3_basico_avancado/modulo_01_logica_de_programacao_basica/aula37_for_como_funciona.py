"""
Iterável ->, range str, etc (__inier__)
iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega o seu iterador
"""

# entendendo como for funciona
texto = iter('Paulo') # __iter__()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())


# numeros = range(5, 10, 1)

# for numero in numeros:
#     print(numero)

