"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
n=int(input("Numero de mes"))

if n==1 or n==2 or n==12:
    print("Invierno")
elif 3<=n<=5:
    print("Primavera")
elif 6<=n<=8:
    print("Verano")
elif 9<=n<=11:
    print("Otoño")
