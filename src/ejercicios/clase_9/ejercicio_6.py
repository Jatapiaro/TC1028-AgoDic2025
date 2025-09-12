"""
Requisito: Dada la frase codigo = "Pyt-h0n 3.9 es genial!":

Itera sobre cada carácter.
Si el carácter es un guion (-) o un espacio (" "), sáltalo (usa continue).
Si el carácter es un número, imprime "¡Error: Se encontró un dígito!" y 
detén el programa (usa break).
Si no es ninguna de las anteriores, añade el carácter al resultado.

Al final, imprime la frase original tras limpiar los carácteres mencionados.

Nota: Investiga el método is_digit()

Ejemplo de ejecución:
>>> Pyt-h0n 3.9 es genial!
Pyth
"""
def main():
    x = input("Introduce una cadena de caracteres")
    acum = ""
    for i in range(0, len(x)):
        if x[i] == "-" or x[i] == " ":
            continue
        if x[i].isdigit():
            break
        acum += x[i]
    print(acum)
main()
