"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
mes = int(input('Introduzca un mes (1-12): '))

if mes == 1 or mes == 2 or mes == 12:
  print('Invierno')
elif mes == 3 or mes == 4 or mes == 5:
  print('Primavera')
elif mes == 6 or mes == 7 or mes == 8:
  print('Verano')
elif mes == 9 or mes == 10 or mes == 11:
  print('Otoño')
else:
  print('Introduzca un mes válido')
