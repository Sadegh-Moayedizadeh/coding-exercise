if __name__ == '__main__':
    numbers = []
    for _ in range(3):
        numbers.append(int(input()))
    numbers.sort(reverse=True)
    if numbers[0]**2 == numbers[1]**2 + numbers[2]**2:
        print('YES')
    else:
        print('NO')
