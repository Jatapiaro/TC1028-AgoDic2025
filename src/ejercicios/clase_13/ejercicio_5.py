"""
Crea un script que guarde una lista de contactos en un archivo
llamado contactos.csv.

Los datos deben tener una cabecera (Nombre, Apellido, Email).
"""

import csv

cabecera = ["Nombre", "Apellido", "Email"]
contactos = [
    ["Juan", "Pérez", "juan.perez@email.com"],
    ["Ana", "García", "ana.garcia@email.com"],
    ["Luis", "Martínez", "luis.martinez@email.com"],
]

PATH = (
    "/Users/jatapiaro/Documents/TC1028-AgoDic2025/src/ejercicios/clase_13/contactos.csv"
)


def main():
    try:
        with open(PATH, mode="w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(cabecera)
            writer.writerows(contactos)
    except PermissionError:
        print("No hay permiso para escribir en ese directorio")


main()
