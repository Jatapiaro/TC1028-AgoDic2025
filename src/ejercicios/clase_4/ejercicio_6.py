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
peso: float = float(input("Ingresa tu peso en kg: "))
estatura: float = float(input("Ingresa tu estatura en metros: "))

imc: float = peso / (estatura ** 2)

print(f"IMC: {imc: .2f} --> ", end="")

if imc < 18.5:
    print("Bajo Peso")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
