"""
Escribe un programa, que dado un string, imprima al usuario el conteo de vocales
de dicho string.
Por ejemplo, la frase "El lenguaje PythOn es muy popUlAr" tiene las siguientes
vocales.

E, e, u, a, e, O, e, u, o, U, A.

En este caso las vocales O y o se cuentan como una sola vocal.
Investiga el uso de la funcion lower() de la clase string.

Ejemplo de ejecución:
>>> El lenguaje PythOn es muy popUlAr

a => 2
e => 4
i => 0
o => 2
u => 2
"""


def main():
    frase = input("Ingrese su frase: ")
    frase = frase.lower()
    a, e, i, o, u = 0, 0, 0, 0, 0

    for x in frase:
        if x == "a":
            a = a + 1
        elif x == "e":
            e = e + 1
        elif x == "i":
            i = i + 1
        elif x == "o":
            o = o + 1
        elif x == "u":
            u = u + 1

    print(f"a = {a}")
    print(f"e = {e}")
    print(f"i = {i}")
    print(f"o = {o}")
    print(f"u = {u}")


main()
