"""
Crea un programa que calcule la suma de números desde 1 hasta un N
dado por el usuario.

Aunque la solución más eficiente es la formula de Gauss, usa un ciclo for.
"""


def main():
    stop = int(input("Stop: "))  # 10
    suma = 0
    # for iterador in range(1, stop + 1):
    for iterador in range(stop):
        suma += iterador + 1

    print(suma)


main()
