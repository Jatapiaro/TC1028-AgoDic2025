"""
Análisis de Votos Electorales

Objetivo: Contar los votos de una elección y declarar un ganador,
usando únicamente listas para almacenar y procesar los datos.

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

"""
def generate_votes_list(
    n_candidates: int = 4, number_of_votes: int = 1_000_000
) -> list[str]:
    candidates = [f"Candidato {i + 1}" for i in range(n_candidates)]
    return random.choices(candidates, k=number_of_votes)
"""
import list_utils


def get_unique_list(votes: list[str]) -> list[tuple[str, int]]:
    unique_list = []

    for candidate_name in votes:
        did_find_candidate = False

        for i in range(len(unique_list)):
            candidate, vote_count = unique_list[i]
            if candidate_name == candidate:
                unique_list[i] = (candidate, vote_count + 1)
                did_find_candidate = True
                break

        if not did_find_candidate:
            unique_list.append((candidate_name, 1))

    return unique_list


def main():
    votes = list_utils.generate_votes_list(n_candidates=5, number_of_votes=100)
    votes_list = sorted(get_unique_list(votes=votes))
    for v in votes_list:
        print(v)


main()
