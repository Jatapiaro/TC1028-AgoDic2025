"""
Los divisores propios de un número n son aquellos divisores positivos menores que
n.
Un número entero positivo n se dice que es perfecto si la suma de sus divisores
propios es igual a n.

Realiza un programa que lea un número y muestre un mensaje indicando si es
perfecto o no.

Ejemplo:
Los divisores de 6 son 1, 2, 3.
Por lo tanto 1 + 2 + 3 = 6

Ejemplos de ejecución del programa:
>>> 6
Es Perfecto

>>> 28
Es perfecto

>>> 121
No es perfecto
"""


def es_perfecto(numero: int) -> bool:
    contador = 1
    suma = 0
    while contador < numero:
        if numero % contador == 0:
            suma += contador

        if suma > numero:
            break
        contador += 1

    if suma == numero:
        return True

    return False


def main():
    numero = int(input("Número: "))
    print(es_perfecto(numero=numero))


main()
