# https://quera.org/problemset/2795/

from typing import Iterable, Tuple


def can_reach_last_floor(
    buildings_guarding_data: Iterable[Iterable[Tuple[int, ...]]]
) -> Iterable[bool]:
    result = []
    for each_building_guarding_data in buildings_guarding_data:
        sorted_data = sorted(each_building_guarding_data, key=lambda x: x[0])
        if len(sorted_data) == 1:
            result.append(True)
            continue
        for index in range(len(sorted_data)):
            if index == 0:
                continue
            current_floor_number = sorted_data[index][0]
            current_floor_guard_position = sorted_data[index][1]
            previous_floor_number = sorted_data[index - 1][0]
            previous_floor_guard_position = sorted_data[index - 1][1]
            if (
                current_floor_number == previous_floor_number + 1 and
                current_floor_guard_position ^ previous_floor_guard_position
            ):
                result.append(False)
                break
            if index == len(sorted_data) - 1:
                result.append(True)
    return result


def get_input() -> Iterable[Iterable[Tuple[int, ...]]]:
    number_of_tests = int(input())
    test_number = 0
    result = []
    for _ in range(number_of_tests):
        each_data = []
        number_of_guards = list(map(int, input().split(' ')))[1]
        for _ in range(number_of_guards):
            each_data.append(tuple(map(int, input().split(' '))))
        result.append(each_data)
    return result


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
    print_results(can_reach_last_floor(get_input()))
