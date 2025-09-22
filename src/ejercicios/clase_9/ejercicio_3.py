"""
Imprime todos los números del 1 al 15 (incluido),
Pero salta (no imprimas) cualquier número que sea múltiplo de 3.
"""


def main():
    for i in range(1, 16):
        if i % 3 == 0:
            continue

        print(i)


main()
