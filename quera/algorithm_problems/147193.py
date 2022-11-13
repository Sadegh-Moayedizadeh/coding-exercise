if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    if a == 0 and b == 0:
        print('infinite')
    elif a == 0:
        print('invalid')
    else:
        print('unique')
