# - Funciones Recursivas - #

# - Primer ejercicio de funciones - #

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print("El factorial de 7 es: ", factorial(7))

# - Segundo ejercicio de funciones - #

# Crear una función recursiva que determine si un número es primo o no.

def primo(n, i = 2):
    if n == 2:
        return True
    elif n < 2 or n % i == 0:
        return False
    elif i > n ** 0.5:
        return True
    else:
        return primo(n, i + 1)
    
print("El numero 89 es primo: ", primo(89))

# - Tercer ejercicio de funciones - #

# Escribir una función recursiva que calcule el n-ésimo término de la serie de Fibonacci.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print("El numero 13 de la serie de Fibonacci es: ", fibonacci(13))