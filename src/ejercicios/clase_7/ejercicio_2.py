"""
Escribe un programa que pida al usuario que introduzca números de forma continua.

El programa debe hacer lo siguiente:
- Sumar únicamente los números que sean positivos.
- Si el usuario introduce un número negativo, el programa debe mostrar un mensaje
indicando que el número no será sumado y continuar pidiendo el siguiente.
- El programa debe detenerse y mostrar la suma total acumulada solo cuando el
  usuario escriba la palabra "fin".

El programa debe mostrar al final la suma total y la cantidad de números que
fueron considerados en la suma.
"""


def main():
    suma_total = 0
    contador = 0

    while True:
        entrada = input("Dame un Número: ")
        if entrada == "fin":
            break

        entrada = int(entrada)
        if entrada < 0:
            continue

        suma_total += entrada
        contador += 1

    print(suma_total, contador)


main()
