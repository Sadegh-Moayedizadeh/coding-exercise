def factorial(n: int) -> int:
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def remove_zeros(n: int) -> int:
    result = n
    while result % 10 == 0:
        result = result // 10
    return result


if __name__ == '__main__':
    print(remove_zeros(factorial(int(input()))) % 10)
