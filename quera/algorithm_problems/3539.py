if __name__ == '__main__':
    number = int(input())
    while number >= 10:
        number = sum(map(int, str(number)))
    print(number)
