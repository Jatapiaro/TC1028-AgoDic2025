"""
Calcula el IMC (peso / (est ** 2))

Entradas:
El peso en kg
La estatura en metros

Salidas: #Se cambia "peso" por "IMC"
- Si IMC menor a 18.5 => Bajo Peso
- Si IMC mayor o igual a 18.5 y menor a 25 => "Normal"
- Si IMC mayor o igual a 25 y menor a 30 => Sobrepeso
- Si IMC mayor o igual a 30 => Obesidad

Ejemplo de ejecución:
>>> 54 #ejemplo en kg
>>> 1.7 #ejemplo de altura

IMC: 18.68 => Normal #Se agrega el "Normal" y se ajustan decimales
"""
peso = float(input("Ingresa tu peso en kg: "))
est = float(input("Ingresa tu estatura en metros: "))
IMC = (peso) / (est ** 2)
if IMC < 18.5:
  print("IMC: ", IMC, "=> Bajo Peso")
elif IMC >= 18.5 and IMC < 25:
  print("IMC: ", IMC, "=> Normal")
elif IMC >= 25 and IMC < 30:
  print("IMC: ", IMC, "=> Sobrepeso")
else:
  print("IMC: ", IMC, "=> Obesidad")
