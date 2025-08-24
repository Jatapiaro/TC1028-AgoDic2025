"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:s
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""


def main():
    month = int(input("Introduce un mes en número: "))

    if month in [1, 2, 12]:
        print("invierno")
    elif month in [3, 4, 5]:
        print("primavera")
    elif month in [6, 7, 8]:
        print("verano")
    elif month in [9, 10, 11]:
        print("0toño")
    else:
        print("mes inválido")


if __name__ == "__main__":
    main()
