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
def main():
    numero_uno = int(input("Ingrese el primer numero: "))
    numero_dos = int(input("Ingrese el segundo numero: "))
    clave = input("Ingrese la clave de la operacion a realizar (s, r, m, d): ")
   
    resultado = operacion(numero_uno, numero_dos, clave)
    print(f"El resultado de la operacion es: {resultado}")

def operacion(numero_uno: int, numero_dos: int, clave: str) -> int:
    if clave == "s":
        return numero_uno + numero_dos
    elif clave == "r":     
        return numero_uno - numero_dos
    elif clave == "m":
        return numero_uno * numero_dos
    elif clave == "d":
        if numero_dos != 0:
            return numero_uno / numero_dos
        else:
            return "Error"
    else:
        return "Clave incorrecta"    
    
if __name__ == "__main__":
    main()
