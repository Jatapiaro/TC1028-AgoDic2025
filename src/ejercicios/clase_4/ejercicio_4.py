"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""

numero = int(input("Introduce un número: "))

if numero < 0:
    print("Negativo")   
elif numero == 0:
    print("Cero")
else:
    print("Positivo")
