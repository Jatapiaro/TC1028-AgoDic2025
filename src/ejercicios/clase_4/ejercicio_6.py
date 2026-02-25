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
kg = float(input("Peso en kg: "))
estatura = float(input("Ingresa la estatura: "))
                 
imc = kg / (estatura ** 2)

if imc < 18.5:
    print(f" IMC: {imc:.2f} => Bajo peso")
elif imc >= 18.5 and imc < 25:
    print(f"IMC: {imc:.2f} => Normal")
elif imc >=25 and imc < 30:
    print(f"IMC: {imc:.2f} => Sobrepeso")
elif imc >= 30:
    print(f"IMC: {imc:.2f} => Obesidad")
