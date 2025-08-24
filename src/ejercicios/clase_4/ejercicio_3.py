"""
Crea un programa que simule el lanzamiento de 2 monedas.
Si ambas monedas caen en la misma cara, el programa deberá imprimir "Ganaste"
De lo contrario el programa deberá imprimir "Perdiste".
"""

import random


def calculation(coin_1, coin_2, coin_3, coin_4):
    return coin_1 + coin_2 + coin_3 + coin_4


def main():
    coin_1 = random.randint(0, 1)
    coin_2 = random.randint(0, 1)
    coin_3 = random.randint(0, 1)
    coin_4 = random.randint(0, 1)

    ans = calculation(coin_1, coin_2, coin_3, coin_4)

    if ans == 0 or ans == 4:
        print("Ganaste")
    else:
        print(f"Perdiste: {coin_1}, {coin_2}, {coin_3}, {coin_4}")


if __name__ == "__main__":
    main()
