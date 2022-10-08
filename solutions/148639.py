# https://quera.org/problemset/148639/


def main(depth: int, call_number: int = 1) -> str:
    if depth == 1:
        return str(call_number)
    return str(call_number) + '+' + '\\frac{{{}}}{{{}}}'.format(
        main(depth - 1, call_number * 2),
        main(depth - 1, call_number * 2 + 1)
    )


def get_input() -> int:
    return int(input())


def print_results(result: str) -> None:
    print(result)


def test() -> None:
    # Arrange
    depth = 3
    expected_fraction = '1+\\frac{2+\\frac{4}{5}}{3+\\frac{6}{7}}'

    # Act
    actual_fraction = main(depth)

    # Assert
    assert actual_fraction == expected_fraction, actual_fraction


if __name__ == '__main__':
    # test()
    print_results(main(get_input()))
