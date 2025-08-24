"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
mes = int(input("Ingresa en número el mes que desee: "))

if mes in (1, 2, 12):
  print("Invierno")
elif mes in (3, 4, 5):
  print("Primavera")
elif mes in (6, 7, 8):
  print("Verano")
elif mes in (9, 10, 11):
  print("Otoño")
else: 
  print("Mes invalido")