# https://quera.org/problemset/148099/

from collections import Counter
from typing import Iterable


def main(numbers: Iterable[int]) -> int:
    counter = Counter(numbers)
    unique_numbers = [number for number, count in counter.items() if count == 1]
    result = 0
    for number in unique_numbers:
        result ^= number
    return result


def get_input() -> Iterable[int]:
    number_of_elements = int(input())
    elements = map(int, input().split(' '))
    return elements


def print_results(result: int) -> None:
    print(result)


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(main(get_input()))
