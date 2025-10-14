"""
Crea un método que, dado una matriz con 5 calificaciónes
por estudiante, calcule el promedio de cada estudiante
y regrese una lista con los promedios.
[p1, p2..., p5]
"""

import random


def crear_matriz(n_alumnos: int, n_calificaciones: int = 5) -> list[list[float]]:
    calificaciones = []
    for _ in range(n_alumnos):
        n_list = [0.0] * n_calificaciones
        calificaciones.append(n_list)

    return calificaciones


def llenar_matriz(matriz: list[list[float]]) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            calificacion = float(random.randint(a=20, b=100))
            matriz[i][j] = calificacion


def calcular_promedios(matriz: list[list[float]]) -> list[float]:
    result = []
    for i in range(len(matriz)):
        suma = 0
        n_calificaciones = len(matriz[i])
        for j in range(n_calificaciones):
            suma += matriz[i][j]

        result.append(suma / n_calificaciones)

    return result


def main():
    n_c = crear_matriz(n_alumnos=26, n_calificaciones=8)
    llenar_matriz(matriz=n_c)
    print(n_c)
    print(calcular_promedios(matriz=n_c))


main()
