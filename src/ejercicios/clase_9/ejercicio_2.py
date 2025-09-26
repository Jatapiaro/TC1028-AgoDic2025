"""
Crea un programa que pida una cadena de texto al usuario.
Por ejemplo, dada la frase "El lenguaje Python es muy popular",
busca la primera vocal "o" (minúscula).

Cuando la encuentres, imprime "¡Vocal 'o' encontrada!" y detén el ciclo
inmediatamente.
"""


def main():
    """
    Hola   Mundo
    0  3 5 6   9
    """
    texto = input("Ingresa una frase: ")
    for i in range(0, len(texto)):
        if texto[i] == "o":
            print(f"¡Vocal 'o' encontrada en indice {i}!")
            break


main()
