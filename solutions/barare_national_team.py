# https://quera.org/problemset/10163/

from collections import defaultdict
from functools import cached_property
from typing import Dict, Iterable, List, Mapping, Tuple


def merge_sorted_iterables(
    first_iterable: Iterable[Tuple[int, str]],
    second_iterable: Iterable[Tuple[int, str]]
) -> Iterable[Tuple[int, str]]:
    first_list = list(first_iterable)
    second_list = list(second_iterable)

    result = []
    while first_list and second_list:
        if first_list[-1] > second_list[-1]:
            result.append(first_list.pop())
        else:
            result.append(second_list.pop())
    if first_list:
        first_list.reverse()
        result.extend(first_list)
    else:
        second_list.reverse()
        result.extend(second_list)

    result.reverse()
    return result


def calculate_cost(
    fees: Mapping[int, int],
    intervals: Iterable[Tuple[int, ...]]
) -> int:
    starts = map(lambda i: (i, 's'), sorted(map(lambda t: t[0], intervals)))
    ends = map(lambda i: (i, 'e'), sorted(map(lambda t: t[1], intervals)))
    points_with_flag = merge_sorted_iterables(starts, ends)

    open_intervals_to_legth: Dict[int, int] = defaultdict(int)
    number_of_open_intervals = 1
    previous_point = None
    for point_with_flag in points_with_flag:
        point = point_with_flag[0]
        if previous_point is None:
            previous_point = point
            continue

        length = point - previous_point
        open_intervals_to_legth[number_of_open_intervals] += length

        flag = point_with_flag[1]
        if flag == 's':
            number_of_open_intervals += 1
        elif flag == 'e':
            number_of_open_intervals -= 1
        previous_point = point

    result = 0
    for number_of_open_intervals, length in open_intervals_to_legth.items():
        if number_of_open_intervals == 0:
            continue
        result += fees[number_of_open_intervals] * length * number_of_open_intervals
    return result


def get_input() -> Tuple[Mapping[int, int], Iterable[Tuple[int, ...]]]:
    fees = list(map(int, input().split(' ')))
    intervals = []
    for _ in range(len(fees)):
        intervals.append(tuple(map(int, input().split(' '))))
    open_interval_lengths_to_fee = {
        index + 1: fee for index, fee in enumerate(fees)
    }
    return open_interval_lengths_to_fee, intervals


def print_results(result: int) -> None:
    print(result)


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(calculate_cost(*get_input()))
