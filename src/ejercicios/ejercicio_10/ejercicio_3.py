"""
Escribe una función que cuente el número de palabras en un string sin usar split().
Función: contar_palabras(texto)
Qué hace: Recibe un string que puede contener espacios al inicio, al final o múltiples espacios entre palabras.
Lógica:
    La idea es contar cuántas veces "empieza" una palabra.
    Usa una variable estado (o "flag") llamada en_palabra (inicializada en False).
    Inicializa contador_palabras = 0.
    Recorre cada caracter del texto con un ciclo for.

Retorno: Debe retornar el contador_palabras.
"""