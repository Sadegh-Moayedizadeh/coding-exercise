if __name__ == '__main__':
    repetition = int(input())
    numbers = []
    for _ in range(repetition):
        numbers.append(int(input()))

    a, b, c = 5, 0, 0
    main_number = 1
    for number in numbers:
        b += 1
        if number == 2:
            c -= 1
    print(a, b, c)
        