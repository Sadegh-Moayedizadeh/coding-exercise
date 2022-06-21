# https://quera.org/problemset/10169/

from typing import Tuple


def main(number_of_rows: int, path: str) -> int:
    number = 1
    for direction in path:
        row_start_number = int(number ** 0.5)
        row_end_number = row_start_number * 2 - 1
        number += (
            (number - row_start_number) * 2 +
            (row_end_number - number) +
            (direction == 'R') + 1
        )
    return 2 ** (number_of_rows + 1) - number


def get_input() -> Tuple[int, str]:
    number_in_string, path = input().split(' ')
    return int(number_in_string), path


def print_results(number: int) -> None:
    print(number)


def test() -> None:
    # Arrange
    number_of_rows = 3
    path = 'LR'
    expected_result = 11

    # Act
    actual_result = main(number_of_rows, path)

    # Assert
    assert actual_result == expected_result


if __name__ == '__main__':
    # test()
    print_results(main(*get_input()))
