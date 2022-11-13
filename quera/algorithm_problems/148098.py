# https://quera.org/problemset/148098/

from typing import Iterable, Tuple


def calculate_number_of_days_to_reach_desired_income(
    desired_income: int, profits: Iterable[int], costs: Iterable[int]
) -> int:
    result = (desired_income + sum(costs)) / sum(profits)
    return int(result) if result % 1 == 0 else int(result) + 1


def number_of_days_to_reach_goal(
    goal: int,
    profit_to_costs: Iterable[Tuple[int, ...]],
    attempts: int
) -> int:
    result = None
    sorted_profit_to_costs = sorted(
        profit_to_costs,
        key=lambda profit_to_cost:
            (
                calculate_number_of_days_to_reach_desired_income(
                    goal, [profit_to_cost[0]], [profit_to_cost[1]]),
                profit_to_cost[1] - profit_to_cost[0]
            )
    )
    profits = list(map(lambda x: x[0], sorted_profit_to_costs))
    costs = list(map(lambda x: x[1], sorted_profit_to_costs))
    for i in range(attempts):
        new_result = calculate_number_of_days_to_reach_desired_income(
            goal, profits[:i + 1], costs[:i + 1])
        if result is None or new_result < result:
            result = new_result
        else:
            return result
    assert result is not None
    return result


def get_input() -> Tuple[int, Iterable[Tuple[int, ...]], int]:
    attempts, goal = map(int, input().split(' '))
    profit_to_cost = []
    for _ in range(attempts):
        profit, cost = map(int, input().split(' '))
        profit_to_cost.append((profit, cost))
    return goal, profit_to_cost, attempts


def print_results(result: int) -> None:
    print(result)


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    print_results(number_of_days_to_reach_goal(*get_input()))
