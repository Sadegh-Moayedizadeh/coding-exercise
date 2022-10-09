# https://quera.org/problemset/147635/

from typing import Iterable


def main(tempratures: Iterable[int]) -> Iterable[str]:
    return [
        'cooler' if temprature > 15 else 'heater'
        for temprature in tempratures
    ]


def get_input() -> Iterable[int]:
    number_of_days = int(input())
    tempratures = map(int, input().split(' '))
    return tempratures


def print_results(results: Iterable[str]) -> None:
    print('\n'.join(results))


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(main(get_input()))
