# - Funciones Anonimas - #

# - Primer ejercicio de funciones - #

lista = [1, 3, 5, 10, 50, 2, 4, 6, 8, 9, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista.sort(key = lambda x: x)

print("Lista ordenada: ", lista)

# - Segundo ejercicio de funciones - #

lista = [1, 3, 5, 10, 50, 2, 4, 6, 8, 9, 7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista2 = list(filter(lambda x: x % 2 == 0, lista))

print("Lista filtrada: ", lista2)

# - Tercer ejercicio de funciones - #

lista = [1, 3, 5, 10, 50, 2, 4, 6, 8, 9, 7,]

lista2 = list(map(lambda x: x ** 2, lista))

print("Lista elevada al cuadrado: ", lista2)
