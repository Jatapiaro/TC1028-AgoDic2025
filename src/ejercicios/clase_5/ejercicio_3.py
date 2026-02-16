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
def operacion(n1, n2, clave):
    if clave == "s":
        return n1 + n2
    elif clave == "r":
        return n1 - n2
    elif clave == "m":
        return n1 * n2
    elif clave == "d":
        return n1 / n2
    else:
        return "Clave inválida"
    
def main():
    print("\nEste programa realiza una operación aritmética con los valores ingresados.")
    valor1: int = int(input("Ingresa el primer número: "))
    valor2: int = int(input("Ingresa el segundo número: "))
    clave: str = input("Ingresa la clave ('s', 'r', 'm' o 'd'): ")
    
    resultado = operacion(valor1, valor2, clave)
    if resultado == "Clave inválida":
        print("\nClave inválida\n")
    else:
        print(f"\nEl resultado es {resultado}\n")

if __name__ == "__main__":
    main()
