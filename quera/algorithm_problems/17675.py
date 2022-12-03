from typing import Set


def find_fibonacci_numbers_under(number: int) -> Set[int]:
    a, b = 1, 1
    result = set()
    while b < number:
        result.add(b)
        a, b = b, b + a
    return result


if __name__ == '__main__':
    number = int(input())
    fibonacci_numbers = find_fibonacci_numbers_under(number)
    for i in range(1, number + 1):
        if i in fibonacci_numbers:
            print('+', end='')
        else:
            print('-', end='')
    print()
