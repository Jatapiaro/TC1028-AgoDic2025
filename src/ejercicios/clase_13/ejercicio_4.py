"""
Escribe un script de Python que lea un archivo e imprima cada línea numerada.
"""

FILE_PATH = "/Users/jatapiaro/Documents/TC1028-AgoDic2025/src/ejercicios/clase_13/lista_de_compras.txt"


def main():
    try:
        with open(FILE_PATH, "r") as archivo:
            for i, linea in enumerate(archivo, 1):
                print(f"{i}: {linea.strip()}")
    except FileNotFoundError:
        print("El archivo no existe")


main()
