# Funciones Definidas #

# - Primer ejercicio de funciones - #

def area_circulo(radio):
    area = 3.1416 * radio ** 2
    return area

from Funciones import area_circulo

print("El area del circulo es: ", area_circulo(5))

# - Segundo ejercicio de funciones - #

def numero_mas_grande(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max

from Funciones import numero_mas_grande

print("El numero mas grande es: ", numero_mas_grande([100, 32, 53, 4, 58, 63, 97, 98, 9, 10]))

# - Tercer ejercicio de funciones - #

def distancia_entre_puntos(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d

from Funciones import distancia_entre_puntos

print("La distancia entre los puntos es: ", distancia_entre_puntos(1, 2, 3, 4))
