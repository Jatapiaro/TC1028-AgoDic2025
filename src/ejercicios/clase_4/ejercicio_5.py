"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
mes = int(input("Ingresa un mes del año en numero 1-12  "))
if mes >=3 and mes <=5:
    print("Te encuentras en Primavera")
elif mes >=6 and mes <=8:
    print("Te encuentras en Verano")
elif mes >=9 and mes <=11:
    print("Te encuentras en Otoño")
else:
    print("Te encuentras en Invierno")
