"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
n = int(input("Ingrese su numero:\n"))
print("negativo" if n < 0 else "cero" if n == 0 else "positivo")
