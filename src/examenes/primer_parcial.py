"""
Problema: Descomposición por valor posicional
Enunciado
Escribe un método que reciba un número entero positivo n > 0 y devuelva una
representación de n como suma de sus componentes por valor posicional.

Por ejemplo, 3452 debe representarse como 3000 + 400 + 50 + 2.
El método no debe imprimir nada; solo debe devolver el resultado.

Además, escribe un main que:
Lea un entero positivo usando input() vacío (sin mensaje dentro):
n = int(input())

Llame a tu método con n.
Imprima únicamente el valor devuelto por el método con:
print(res)

Se penaliza cualquier impresión con texto adicional, p. ej.:
print("El resultado es", res) o print(f"el resultado es {res}").

La salida debe estar separada por “ + ” entre términos.
Si el resultado deja un “+” extra al final, está bien (no se penaliza).
Por ejemplo si la entrada es 152 y el resultado lo muestras como 150 + 52 + 2 +,
no se penalizará.
No se puede usar conversión del número original a texto para resolver la
descomposición ni funciones/métodos de cadenas (por ejemplo: str(n) para
inspeccionar dígitos, split, slicing de strings, indexar strings, etc.).

Únicamente se permite usar ''.join(lista) si  es que sabes como usuarlo.
Puedes convertir al final los términos ya obtenidos (p. ej., 3000, 600, 9) a
texto para imprimirlos; lo que no se permite es convertir el número original a texto para analizar sus dígitos.

El método debe devolver el resultado como un string. Es decir, el resultado no
se debe imprimir dentro del método que hayas creado.

Formato de entrada
Un solo entero positivo n > 0 leído con input() sin mensaje.

Formato de salida
Una línea con la descomposición, por ejemplo:
3000 + 400 + 50 + 2
(o con un + final, también aceptado).

Casos de ejemplo (esperados)
3452 → 3000 + 400 + 50 + 2

Caso no tan intuitivo: 2609 → 2000 + 600 + 9 (el 0 en las decenas no aparece)

7 → 7

90 → 90

1005 → 1000 + 5

1010 → 1000 + 10

999 → 900 + 90 + 9

1000 → 1000
"""


def find_first_power_of_ten_for_number(number: int) -> int:
    start = 1
    while start < number:
        start *= 10

    return start


def decompose_number(number: int) -> str:
    divisor = find_first_power_of_ten_for_number(number=number)
    result = ""
    while divisor > 0:
        first_digit = number // divisor
        if first_digit != 0:
            # Divide 223 by 100, is 2. 2 times 100 is 200
            result += f"{first_digit * divisor} + "

        number = number % divisor  # If number was 223, modulus 100 is 23
        divisor //= 10

    # I'm always adding " + " as suffix in line 75...remove it
    return result.removesuffix(" + ")


def main():
    print(decompose_number(number=int(input())))


main()
