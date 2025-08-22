"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
n=float(input("Coloca tu numero"))

if n==0:
    print("cero")
elif n>0:
    print("Positivo")
else:
    print("Negativo")
