"""
Simula un cajero con un saldo inicial.

Lógica:
Define una variable saldo = 1000.

Usa un ciclo while True para mostrar un menú de opciones:
Consultar Saldo
Depositar
Retirar
Salir

Pide al usuario que elija una opción (un número del 1 al 4).
Decisiones: Usa if/elif/else para manejar la opcion elegida:
    Opción 1: Imprime el saldo actual.
    Opción 2 (Depositar): Pide al usuario una cantidad.
        Usa un mini-ciclo while para validar que la cantidad sea positiva. Luego, suma la cantidad al saldo.

    Opción 3 (Retirar): Pide al usuario una cantidad. Usa if/elif para validar:
        Si la cantidad es negativa, imprime "Monto no válido".
        Si la cantidad es mayor que el saldo, imprime "Fondos insuficientes".
        Si es válida, resta la cantidad del saldo.

    Opción 4 (Salir): Imprime "Gracias por usar el cajero." y usa break para terminar el ciclo.
    else: Si la opción no es 1, 2, 3 o 4, imprime "Opción no válida."
"""
