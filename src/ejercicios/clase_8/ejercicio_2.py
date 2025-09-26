"""
Cuenta dígitos
Escribe un programa que lea un número entero positivo y que muestre en la
pantalla la cantidad de dígitos que tiene.

Sugerencia: Divide el número entre 10 repetidamente hasta que el número sea
menor que 1.

325 // 10 = 32
32 // 10 = 3
3 // 10 = 0

Entrada
Un número entero positivo

Salida
La cantidad de dígitos que tiene el número ingresado
Ejemplo de ejecución del programa:

>>>>4258

4
"""


def metodo(num: int) -> int:
    contador = 0
    while num >= 1:
        num //= 10  # num = num // 10
        contador += 1  # contador = contador + 1

    return contador


def main():
    n = int(input("Num: "))
    print(metodo(num=n))


main()
