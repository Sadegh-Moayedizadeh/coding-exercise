from typing import Iterable


def evaluate_maximum_sum(
    triangle: Iterable[Iterable[int]],
    i: int = 0,
    j: int = 0,
    cache = None
) -> int:
    if cache is None:
        cache = {}

    if (i, j) in cache:
        return cache[(i, j)]

    if i == len(triangle) - 1:
        cache[(i, j)] = triangle[i][j]
        return triangle[i][j]

    result = triangle[i][j] + max(
        evaluate_maximum_sum(triangle, i + 1, j, cache),
        evaluate_maximum_sum(triangle, i + 1, j + 1, cache)
    )
    cache[(i, j)] = result
    return result


def get_inputs() -> Iterable[Iterable[Iterable[int]]]:
    result = []
    numeber_of_triangles = int(input())
    for _ in range(numeber_of_triangles):
        number_of_rows = int(input())
        this_triangle = []
        for _ in range(number_of_rows):
            this_triangle.append(list(map(int, input().split(' '))))
        result.append(this_triangle)
    return result


if __name__ == '__main__':
    for triangle in get_inputs():
        print(evaluate_maximum_sum(triangle))
