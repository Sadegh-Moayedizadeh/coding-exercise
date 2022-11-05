# https://quera.org/problemset/64435/

from typing import Iterable, List


def calculate_area_under_line(plain: List[List[str]]) -> float:
    reversed_plain = list(zip(*plain))
    area = 0
    for column in reversed_plain:
        reached_line = False
        for cell in column:
            if cell == '/':
                reached_line = True
                area += 0.5
            elif cell == '\\':
                reached_line = True
                area += 0.5
            elif cell == '_':
                reached_line = True
            elif cell == '.' and reached_line:
                area += 1
    return area


def main(plains: Iterable[List[List[str]]]) -> Iterable[float]:
    return map(calculate_area_under_line, plains)


def print_results(areas: Iterable[float]) -> None:
    for area in areas:
        print(area)


def get_input() -> Iterable[List[List[str]]]:
    number_of_plains = int(input())
    plains = []
    while number_of_plains:
        number_of_columns, number_of_rows = map(int, input().split(' '))
        plain = []
        for _ in range(number_of_columns):
            plain.append(list(input()))
        plains.append(plain)
        number_of_plains -= 1
    return plains


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(main(get_input()))
