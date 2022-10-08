# https://quera.org/contest/assignments/44345/problems/148509

from typing import Iterable, Tuple


def calculate_result(
    games: Iterable[Iterable[Tuple[int, ...]]]
) -> Iterable[str]:
    result = []
    for game in games:
        if game[0][0] + game[1][0] > game[0][1] + game[1][1]:
            result.append('perspolis')
        elif game[0][0] + game[1][0] < game[0][1] + game[1][1]:
            result.append('esteghlal')
        elif game[0][1] > game[1][0]:
            result.append('esteghlal')
        elif game[0][1] < game[1][0]:
            result.append('perspolis')
        else:
            result.append('penalty')
    return result


def get_input() -> Iterable[Iterable[Tuple[int, ...]]]:
    number_of_games = int(input())
    result = []
    for game_number in range(number_of_games):
        goals = list(map(int, input().split(' ')))
        result.append([(goals[0], goals[1]), (goals[2], goals[3])])
    return result


def print_results(results: Iterable[str]) -> None:
    print('\n'.join(results))


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(calculate_result(get_input()))
