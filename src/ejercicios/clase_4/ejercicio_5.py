"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
mes = int(input("Ingresa el mes en numero: "))
if mes == 1 or mes == 2 or mes == 12:
  print("Invierno")
elif mes >= 3 and mes <= 5:
  print("Primavera")
elif mes >= 6 and mes <= 8:
  print("Verano")
else:
  print("Otoño")
