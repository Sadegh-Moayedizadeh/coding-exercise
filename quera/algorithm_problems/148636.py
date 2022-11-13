# https://quera.org/problemset/148636/

from typing import Iterable, Tuple


class List:
    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = list(numbers)

    def insert(self, index: int, new_number: int) -> None:
        self._numbers[index - 1] = new_number

    def is_interval_in_order(self, first_index: int, second_index: int) -> bool:
        list_under_query = self._numbers[first_index - 1: second_index]
        return (
            max(list_under_query) == second_index - first_index + 1
            and len(list_under_query) == len(set(list_under_query))
        )


def main(numbers: Iterable[int], commands: Iterable[str]) -> Iterable[bool]:
    numbers_list = List(numbers)
    result = []
    for command in commands:
        first_letter, second_letter, third_letter = command.split(' ')
        if first_letter == '+':
            numbers_list.insert(int(second_letter), int(third_letter))
        elif first_letter == '?':
            result.append(numbers_list.is_interval_in_order(int(second_letter), int(third_letter)))
    return result


def get_input() -> Tuple[Iterable[int], Iterable[str]]:
    number_of_elements, number_of_rows = map(int, input().split(' '))
    numbers = map(int, input().split(' '))
    commands = []
    for _ in range(number_of_rows):
        commands.append(input())
    return numbers, commands


def print_results(results: Iterable[bool]) -> None:
    for result in results:
        if result:
            print('YES')
        else:
            print('NO')


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(main(*get_input()))
