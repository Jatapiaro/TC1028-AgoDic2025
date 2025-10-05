import random


def generate_list_of_n_items(items) -> list[int]:
    return [item for item in range(items)]


def generate_votes_list(
    n_candidates: int = 4, number_of_votes: int = 1_000_000
) -> list[str]:
    candidates = [f"Candidato {i + 1}" for i in range(n_candidates)]
    return random.choices(candidates, k=number_of_votes)
