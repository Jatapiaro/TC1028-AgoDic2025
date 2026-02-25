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
peso = float(input("Ingresa tu peso  " ))
est = float(input("Ingresa tu estatura   "))

imc = peso / (est**2) 
if imc < 18.5:
    print(f"Bajo de peso, {imc: .2f}")
elif imc >= 18.5 and imc <= 25:
    print(f"Peso normal, {imc: .2f}")
elif imc >= 25 and imc <= 30:
    print(f"Sobrepeso, {imc: .2f}")
else:
    print(f"Obesidad, {imc: .2f}")
