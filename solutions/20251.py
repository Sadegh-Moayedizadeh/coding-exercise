# https://quera.org/problemset/20251/

from collections import defaultdict
from typing import Dict, List


def calculate_bill(
    adjacency_matrix: Dict[int, List[int]],
) -> int:
    number_of_calls = 0

    def inner(root: int) -> int:
        nonlocal number_of_calls
        number_of_calls += 1
        if not adjacency_matrix[root]:
            return 1

        number_of_calls_at_start = number_of_calls
        direct_children_bill = 0
        for child in adjacency_matrix[root]:
            direct_children_bill += inner(child)

        number_of_calls_at_end = number_of_calls
        return (
            (number_of_calls_at_end - number_of_calls_at_start) +
            direct_children_bill + 1
        )
    
    return inner(1)


def get_input() -> Dict[int, List[int]]:
    number_of_nodes = int(input())
    adjacency_matrix = defaultdict(list)
    input_numbers = list(map(int, input().split(' ')))
    for i in range(1, number_of_nodes):
        parent = input_numbers[i - 1]
        child = i + 1
        adjacency_matrix[parent].append(child)
    return adjacency_matrix


def print_results(result: int) -> None:
    print(result)


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(calculate_bill(get_input()))
