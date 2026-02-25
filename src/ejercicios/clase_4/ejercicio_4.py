"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""

i: float = float(input("Ingresa un numero: "))

if i < 0:
    print("Negativo")
elif i == 0:
    print("Cero")
else:
    print("Positivo")
