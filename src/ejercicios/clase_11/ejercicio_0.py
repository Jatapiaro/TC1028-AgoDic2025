import list_utils

"""
def generate_list_of_n_items(items) -> list[int]:
    return [item for item in range(items)]
"""


def main():
    items = list_utils.generate_list_of_n_items(items=10)
    print(items)

    i = 2
    # print(items[0], items[i], items[-1])
    # print(items[start:end:step])
    print(f"Antes de append {len(items)}, {str(items)}")
    items.append("Hola")
    print(f"Después de append {len(items)}, {str(items)}")

    # Remueve elemento usando indice
    value_at_5 = items.pop(5)
    print("Remueve 5", items)
    items.insert(5, value_at_5)
    print("Agrega 5 de nuevo", items)

    # Remueve la primera ocurrencia del valor
    items += [3, 3, 3]
    print(items)
    for _ in range(items.count(3)):
        items.remove(3)
    print(items)

    new_list = [1] * 10
    print(new_list)
    new_list.remove(1)
    print(new_list.count(1))

    new_list = [1, 2, 3]
    new_list.extend([2, 3, 10, [], ["hola", "1", []]])
    print(new_list)


main()
