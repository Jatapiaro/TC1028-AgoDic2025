"""
Objetivo: Usar un bucle while para añadir elementos a una lista hasta que el
usuario decida parar. La condición para detenerse es que el usuario escriba
la palabra "salir".

Después de escribir salir, imprime todas las canciones de forma aleatoría.

Instrucciones:
Este programa te permitirá añadir tantas canciones como quieras a tu playlist.
Cuando termines, solo escribe "salir".
"""

import random


def main():
    playlist = [
        "Poker Face",
        "Amarrame",
        "Perdoname",
        "No Fue",
        "Labios Rotos",
        "Hasta la Raíz",
        "Azul",
        "Cafe con Ron",
        "Let me Love You",
    ]
    while True:
        song = input("Dame una canción: ")
        if song == "salir":
            break

        playlist.append(song)

    # while playlist: es igual a while len(playlist) > 0
    # while len(playlist) > 0:
    #    index_to_remove = random.randint(0, len(playlist) - 1)
    #    song = playlist[index_to_remove]
    #    #playlist.pop(index_to_remove)
    #    playlist.remove(song)
    #    print(song)

    while playlist:
        index_to_remove = random.randint(0, len(playlist) - 1)
        song = playlist[index_to_remove]
        print(song)
        playlist = playlist[:index_to_remove] + playlist[index_to_remove + 1 :]

    print(playlist)


main()
