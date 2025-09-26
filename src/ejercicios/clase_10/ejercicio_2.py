"""
Escribe una función que pida números al usuario hasta que este ingrese un 0,
y al final reporte estadísticas.

Función: calcular_estadisticas()

Qué hace: No recibe parámetros.

Lógica:
    Inicializa variables: contador = 0, suma = 0, minimo = None, maximo = None.
    Usa un ciclo while True para pedir un número al usuario.
    Decisiones:
        Si el número es 0, usa break para salir del ciclo.
        Si es el primer número ingresado (contador == 0), inicializa minimo y maximo con ese número.
        Compara el número con minimo y maximo actuales para actualizarlos si es necesario.

    Aritmética: Acumula la suma y aumenta el contador en cada iteración (excepto con el 0).

Resultado: Cuando el ciclo termine (y si contador > 0),
imprime el total de números, la suma, el promedio (suma / contador),
el número mínimo y el número máximo.
"""


def calcular_estadisticas():
    contador = 0
    suma = 0
    minimo = float("inf")
    maximo = float("-inf")

    while True:
        num = int(input())
        if num == 0:
            break

        contador += 1
        suma += num
        minimo = min(minimo, num)
        maximo = max(maximo, num)

    print(contador, suma, (suma / contador), minimo, maximo)


def main():
    calcular_estadisticas()


main()
