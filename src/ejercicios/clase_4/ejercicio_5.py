"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
m = int(input("Ingrese mes del año:\n"))
print("Invierno" if m in [12,1,2] else "Primavera" if m in [3,4,5] else "Verano" if m in [6,7,8] else "Otoño")
