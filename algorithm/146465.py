# https://quera.org/problemset/146465/


def main() -> None:
    pass


def get_input() -> None:
    pass


def print_results() -> None:
    pass


def test() -> None:
    # Arrange
    # Act
    # Assert
    pass


if __name__ == '__main__':
    # test()
    # print_results(main(*get_input()))
    len_of_list, len_of_sub_list = map(int, input().split(' '))
    if len_of_list % len_of_sub_list == 0:
        print('YES')
    else:
        print('NO')
