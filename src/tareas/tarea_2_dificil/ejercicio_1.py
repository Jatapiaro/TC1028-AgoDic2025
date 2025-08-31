"""
Crea un método que devuelva un tablero de bingo
- Un tablero de bingo se conforma de una tabla de 5 filas por 5 columnas.
- Cada celda esta compuesta por un número aleatorio de 1 a 99
- Dicho número no se puede repetir.

Tú método no deberá devolver una de estas dos opciones:
- Una lista con los 25 números
- Una matriz (lista de listas), donde cada lista en la lista sea de 5 números

Adicionalmente deberás crear un segundo método llamado
imprime_tablero, que reciva la lista del primer método y la imprima de la
siguiente manera

11,  2,  33, 4, 5
 6, 99,  8,  9, 10
11, 12, 13, 14, 15
61, 17, 78, 19, 20
29, 90, 93, 24, 99

Es decir, 5 números por fila.
Importante: No importa si dejas espacios o no entre los números
pero si debe haber comas entre cada número y salto de línea entre cada fila.

Hint:
- Investiga el método ",".join(some_array)
- ¿Cómo sabrías que un número ya fue agregado al tablero?
    - Recuerda que un arreglo de 10 digitos tiene 0 index
    - Es decir, si tiene 10 elementos, los indices de tu arreglo van de 0-9
    - Si fuera de 22 elementos, tus indices van de 0 a 21.
    - ¿Crees que esto sea últil para resolver el problema?
"""
import numpy as np
import random

def generar_tablero() -> list:
    numeros: list = random.sample(range(1, 100), 25)
    tablero: list = np.array(numeros).reshape(5, 5).tolist()
    return tablero

def imprimir_tablero(tablero: list) -> None:
    for fila in tablero:
        print(", ".join(map(str, fila)))

def main():
    tablero: list = generar_tablero()
    imprimir_tablero(tablero)

if __name__ == "__main__":
    main()
