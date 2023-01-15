if __name__ == '__main__':
    n = int(input())
    password = input()
    result = 0
    while n > 0:
        roll = input()
        key = password[len(password) - n]
        result += min(roll.index(key), len(roll) - roll.index(key))
        n -= 1
    print(result)
