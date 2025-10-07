def add_n_to_numbers(a: int, b: int, n: int = 1) -> None:
    a += n
    b += n
    print(a, b)


def add_n_to_list_items(items: list[int], n: int = 1) -> None:
    for i in range(len(items)):
        items[i] += n


def main():
    argument_a = 2
    argument_b = 4
    add_n_to_numbers(a=argument_a, b=argument_b)
    print(f"Originales: {argument_a}, {argument_b}")

    one_list = [1, 2, 3, 4, 5]
    print(f"Original list: {one_list}")
    add_n_to_list_items(items=one_list)
    print(f"After add N: {one_list}")


main()
