"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
mes: int = int(input("¿Qué mes es (1-12)? "))

if 3 <= mes <= 5:
    print("Primavera")
elif 6 <= mes <= 8:
    print("Verano")
elif 9 <= mes <= 11:
    print("Otoño")
else:
    print("Invierno")
