"""
Crea un método que dado una matriz, genere la matriz
transpuesta.

Esto significa: Intercambiar las filas por columnas de una matriz

Matriz Original:
[1, 2, 3]
[4, 5, 6]

Matriz Transpuesta:
[1, 4]
[2, 5]
[3, 6]
"""


def imprimir_matriz(m: list[list[int]]) -> None:
    for i in range(len(m)):
        print(m[i])


def traspuesta(matriz: list[list[int]]) -> list[list[int]]:
    traspuesta = []
    rows = len(matriz)
    cols = len(matriz[0])
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matriz[j][i])
        traspuesta.append(new_row)

    return traspuesta


def main():
    m = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    imprimir_matriz(m=m)
    print("----")
    imprimir_matriz(m=traspuesta(matriz=m))


main()
