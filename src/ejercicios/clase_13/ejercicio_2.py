"""
Leer el contenido de un archivo
Crea un script que abra el archivo nombre.txt que creaste en el ejercicio anterior.

Lee su contenido y muéstralo en la consola con un mensaje de bienvenida.
"""

FILE_PATH = (
    "/Users/jatapiaro/Documents/TC1028-AgoDic2025/src/ejercicios/clase_13/nombre.txt"
)


def main():
    try:
        with open(FILE_PATH, "r") as archivo:
            nombre = archivo.read()
            print(f"{nombre}")
    except FileNotFoundError:
        print("El archivo no existe")


main()
