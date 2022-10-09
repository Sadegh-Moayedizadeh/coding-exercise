# https://quera.org/problemset/145639/


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
    start, finish, length_of_exam, arrival = map(int, input().split(' '))
    if arrival < start:
        print('exam did not started!')
    elif arrival >= finish:
        print('exam finished!')
    elif (finish - arrival) > length_of_exam:
        print(length_of_exam)
    else:
        print(finish - arrival)
