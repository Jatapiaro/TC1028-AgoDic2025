"""
Ejercicio 3
Escribe una función que reciba como parámetro 2 números enteros y una clave que
es una letra.

La clave representa una operación aritmética de acuerdo con la siguiente tabla:

Clave Significado

s        Suma
r        Resta
m       Multiplicación
d        División

La función debe aplicar la operación aritmética a los 2 valores recibidos y
regresar como valor de retorno el resultado de dicha operación.

Nota que dentro de la función no mostrarás nada, solo regresarás el valor usando return.

Escribe ahora una función main en la que pidas al usuario teclear 2 valores
numéricos y una clave (s, r, m, d), después llama la función con los parámetros
correspondientes y luego muestra el resultado de la operación que regresó la función.

Entradas
valor 1
valor 2
clave

Salidas
El resultado de la operación que se especifica con la clave

Ejemplos de ejecución del programa
>>>5
>>>3
>>>r

>>>10
>>>2
>>>m
20
"""
def suma(valor1: float, valor2:float) -> float:
    return valor1 + valor2

def resta(valor1: float, valor2:float) -> float:
    return valor1 - valor2

def multiplicacion(valor1: float, valor2:float) -> float:
    return valor1 * valor2

def division(valor1: float, valor2:float) -> float:
    return valor1 / valor2

def main():
    n1 = float(input("Primer valor: "))
    n2 = float(input("Segundo valor: "))
    clave = input("Clave: ")
    
    if clave == "s":
        res = suma(valor1 = n1, valor2 = n2)
        print(f"La suma de los valores es : {suma(valor1 = n1, valor2 = n2)}")
    
    elif clave == "r":
        res = resta(valor1 = n1, valor2 = n2)
        print(f"La resta de los valores es : {resta(valor1 = n1, valor2 = n2)}")
    
    elif clave == "m":
        res = multiplicacion(valor1 = n1, valor2 = n2)
        print(f"La multiplicacion de los valores es : {multiplicacion(valor1 = n1, valor2 = n2)}")
    
    elif clave == "d":
        res = division(valor1 = n1, valor2 = n2)
        print(f"La division de los valores es : {division(valor1 = n1, valor2 = n2)}")
    
    else:
        print("Opcion no valida")

main()
