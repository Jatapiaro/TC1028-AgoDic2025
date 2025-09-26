"""
Suma de dígitos
Escribe un programa que despliegue la suma de los dígitos de un número entero,
el número puede ser positivo o negativo, la suma siempre será positiva.

Entrada

Un número entero (positivo o negativo)

Salida
Un número entero que representa la suma de los dígitos del número proporcionado
como entrada. Si el número es negativo, la suma será positiva (ver ejemplos).

2975 // 10 = 297
2975 % 10 = 5

Ejemplo del programa en ejecución
>>> 2975 => 2 + 9 + 7 + 5 => 23
23

>>> -517
13
"""


def metodo(num: int) -> int:
    num = abs(num)

    suma = 0
    while num >= 1:
        digito = num % 10
        suma += digito
        num //= 10

    return suma


def main():
    n = int(input("Num: "))
    print(metodo(num=n))


main()
