"""
Calcula el IMC (peso / (est ** 2))

Entradas:
El peso en kg
La estatura en metros

Salidas:
- Si peso menor a 18.5 => Bajo Peso
- Si peso mayor o igual a 18.5 y menor a 25 => "Normal"
- Si peso mayor o igual a 25 y menor a 30 => Sobrepeso
- Si peso mayor o igual a 30 => Obesidad

Ejemplo de ejecución:
>>> 1
>>> 2

IMC: 18.7 => Obesidad
"""

import math


def calculate_bmi(weight, height):
    return weight / math.pow(height, 2)


def main():
    weight = float(input("Introduce tu peso (kg): "))
    height = float(input("Introduce tu altura (m): "))

    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        print("bajo peso")
    elif 18.5 <= bmi < 25:
        print("normal")
    elif 25 <= bmi < 30:
        print("sobrepeso")
    else:
        print("obesidad")


if __name__ == "__main__":
    main()
