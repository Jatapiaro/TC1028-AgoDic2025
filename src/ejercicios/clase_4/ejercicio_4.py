"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
num = input("Ingresa un numero: ")
if num < 0:
  print("Negativo")
elif num == 0:
  print("Cero")
else:
  print("Positivo")
