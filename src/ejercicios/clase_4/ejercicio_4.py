"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
x = int ( input("Ingresa un número"))
if x < 0:
    print("Negativo")
elif x == 0:
    print("Cero")
else:
    print("positivo")
