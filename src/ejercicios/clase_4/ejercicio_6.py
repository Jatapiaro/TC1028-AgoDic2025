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
peso = float(input("Peso (kg): "))
altura = float(input("Estatura (m): "))
imc = peso / altura**2
print("Bajo Peso" if imc < 18.5 else "Normal" if imc < 25 else "Sobrepeso" if imc < 30 else "Obesidad")
