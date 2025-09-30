"""
Análisis de Votos Electorales

Objetivo: Contar los votos de una elección y declarar un ganador, usando únicamente listas para almacenar y procesar los datos.

Descripción:
Partes con una única lista que contiene todos los votos emitidos, 
donde cada elemento es el nombre de un candidato.

votos = ['Candidato A', 'Candidato B', 'Candidato A', 'Candidato C', 'Candidato A']

El programa debe, en orden:
Crear una lista de candidatos únicos: 
- Recorre la lista votos y genera una nueva lista llamada candidatos
  que no contenga nombres repetidos.

- Contar los votos para cada uno
- Declarar al ganador: Encuentra el número más alto en conteo_votos, 
   obtén su índice y úsalo para encontrar el nombre del ganador en la lista 
   candidatos.
"""
