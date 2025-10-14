from collections import defaultdict


def list_intersection(list_a: list[int], list_b: list[int]) -> list[int]:
    if not list_a or not list_b:
        return []

    copy_of_b = [(x, False) for x in list_b]
    for item in list_a:
        for i in range(len(copy_of_b)):
            number, used = copy_of_b[i]
            if not used and number == item:
                copy_of_b[i] = (number, True)
                break

    return [item[0] for item in copy_of_b if item[1]]


def list_intersection_with_dict(list_a: list[int], list_b: list[int]) -> list[int]:
    if not list_a or not list_b:
        return []

    ocurrences: dict[int, int] = defaultdict(int)
    result = []
    for item in list_a:
        ocurrences[item] += 1

    for item in list_b:
        if item in ocurrences and ocurrences[item] > 0:
            result.append(item)
            ocurrences[item] -= 1

    return result


def main():
    a = [4, 9, 1, 17, 11, 26, 28, 54, 69, 9]
    b = [9, 9, 74, 21, 45, 11, 63, 28, 26]
    print(list_intersection(list_a=a, list_b=b))
    print(list_intersection_with_dict(list_a=a, list_b=b))


main()
