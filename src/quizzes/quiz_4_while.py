"""
Problema
Un número Armstrong (o narcisista) es aquel que es igual a la suma de sus dígitos elevados a la potencia del número de dígitos.

Por ejemplo:

153 = 1^3 + 5^3 + 3^3 → Armstrong 

9474 = 9^4 + 4^4 + 7^4 + 4^4 → Armstrong 

123 = 1^3 + 2^3 + 3^3 → no Armstrong

Escribe una función que determine si un número entero positivo n es un número Armstrong.
"""


def count_digits(number: int) -> int:
    digits_count = 0
    divisor = 1
    while divisor < number:
        digits_count += 1
        divisor *= 10

    return digits_count


def is_armstrong(number: int) -> bool:
    # Use an aux var to avoid touching the original number
    aux = number

    n_digits = count_digits(number=number)
    count = 0
    while aux > 0:
        last_digit = aux % 10
        count += last_digit**n_digits
        aux //= 10

    return count == number


def main():
    print(is_armstrong(number=int(input())))


main()
