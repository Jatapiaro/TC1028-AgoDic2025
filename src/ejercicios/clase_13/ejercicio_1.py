"""
Escribir en un archivo nuevo
Crea un script de Python que le pida al usuario su nombre.

Guarda el nombre en un archivo llamado nombre.txt.
"""


def main():
    nombre = input("Nombre: ")
    with open(
        "/Users/jatapiaro/Documents/TC1028-AgoDic2025/src/ejercicios/clase_13/nombre.txt",
        "w",
    ) as archivo:
        archivo.write(nombre)


main()
