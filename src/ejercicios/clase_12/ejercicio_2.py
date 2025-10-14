"""
Crea un método que dado una matriz,
calcule la suma de la diagonal.
"""

import random


def crear_matriz(n_rows: int = 5) -> list[list[int]]:
    matriz = []
    for _ in range(n_rows):
        fila = []
        for _ in range(n_rows):
            fila.append(random.randint(0, 100))
        matriz.append(fila)

    return matriz


def imprimir_matriz(m: list[list[int]]) -> None:
    for i in range(len(m)):
        print(m[i])


def suma_diagonal(m: list[list[int]]) -> int:
    suma = 0
    for i in range(len(m)):
        suma += m[i][i]

    return suma


def main():
    m = crear_matriz()
    imprimir_matriz(m=m)
    print(suma_diagonal(m=m))


main()
