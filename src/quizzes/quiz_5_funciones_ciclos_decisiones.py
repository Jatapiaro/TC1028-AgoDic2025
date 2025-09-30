"""
Problema: Racha de Caracteres Más Larga

** Enunciado **
Escribe un método que reciba una cadena de texto y encuentre el carácter que
tiene la racha consecutiva más larga. El método debe procesar la cadena y
devolver dos valores: el carácter de la racha más larga y la longitud de dicha
racha. El método NO debe imprimir nada, solo devolver los dos valores.

El bloque de código principal (main) debe hacer lo siguiente:
1. Leer una cadena de texto usando input().
2. Llamar al método creado para recibir los dos valores (el carácter y la longitud).
3. Usar esos valores devueltos para imprimir el resultado final.

** Reglas Adicionales **
* Si la cadena de entrada está vacía, el método debe devolver el string "" y
el número 0.

* Si dos o más caracteres empatan con la misma longitud de racha máxima,
el método debe devolver el carácter de la PRIMERA racha que apareció en la cadena.

---
** Formato de Entrada **
Una sola línea de texto.

---
** Formato de Salida **
El bloque main debe imprimir una única línea con el siguiente formato exacto:
Caracter: [c], Longitud: [l]
Para una cadena vacía, la salida debe ser: Caracter: , Longitud: 0

---
** Casos de Ejemplo **
Entrada: abcdeeeeeffgihjayehhhh
Salida Esperada: Caracter: e, Longitud: 5

Entrada: aabbbccccddaaaaa
Salida Esperada: Caracter: a, Longitud: 5

Entrada: aaabbbaaa
Salida Esperada: Caracter: a, Longitud: 3

Entrada: abbcccddddcccbba
Salida Esperada: Caracter: d, Longitud: 4

Entrada: !
Salida Esperada: Caracter: !, Longitud: 1

Entrada: (una línea vacía)
Salida Esperada: Caracter: , Longitud: 0
"""


def longest_repeating_character_substring(text: str) -> tuple[int, str]:
    max_count, max_char = 0, ""
    current_count, current_char = 0, ""

    for char in text:
        if char == current_char:
            current_count += 1
            continue

        if current_count > max_count:
            max_char = current_char
            max_count = current_count

        current_count = 1
        current_char = char

    if current_count > max_count:
        max_char = current_char
        max_count = current_count

    return max_count, max_char


def main():
    count, char = longest_repeating_character_substring(text=input())
    print(f"Caracter: {char}, Longitud: {count}")


main()
