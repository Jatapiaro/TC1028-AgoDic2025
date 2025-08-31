"""
Crea un método que convierta un número entero a número romano.

Entradas:
- El Número entero a convertir.
    - El número tendra un rango de 1 a 3999

Ejemplo de ejecución:
>>> 3749
MMMDCCXLIX

>>> 58
LVIII

>>> 1994
MCMXCIV
"""

def entero_a_romano(entero: int) -> str:
    romano: str = ""
    valores: list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    for valor, simbolo in valores:
        if entero >= valor:
            n: int = entero // valor
            romano += simbolo * n
            entero -= valor * n

    return romano

def main():
    entero: int = int(input("\nIngresa el número entero: "))
    romano: str = entero_a_romano(entero)

    print(f"\n{entero} en números romanos es {romano}\n")

if __name__ == "__main__":
    main()
