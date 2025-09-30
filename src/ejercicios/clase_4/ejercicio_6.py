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
peso = float(input('Introduzca su peso en kg: '))
est = float(input('Introduzca su altura en metros: '))

imc = (peso / (est ** 2))
if  imc < 18.5:
  print('Bajo Peso')
elif imc == 18.5 or imc < 25:
  print('Normal')
elif imc >= 25 or imc < 30:
  print('Sobrepeso')
elif imc >= 30:  
  print('Obesidad')
else:
  print('Error, vuelva a introducir sus datos')
