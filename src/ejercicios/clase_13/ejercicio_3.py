"""
Crea un script que le pregunte al usuario su ciudad.

Añade la ciudad en una nueva línea dentro del archivo nombre.txt,
sin borrar el nombre que ya estaba.
"""

FILE_PATH = (
    "/Users/jatapiaro/Documents/TC1028-AgoDic2025/src/ejercicios/clase_13/nombre.txt"
)


def main():
    try:
        with open(FILE_PATH, "a") as archivo:
            archivo.write("\n CDMX")
    except FileNotFoundError:
        print(f"El archivo {FILE_PATH} no existe")


main()
