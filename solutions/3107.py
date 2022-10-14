if __name__ == '__main__':
    target_sizes = map(int, input().split(' '))
    actual_sizes = map(int, input().split(' '))
    if all(
        target_size >= actual_size
        for target_size, actual_size
        in zip(target_sizes, actual_sizes)
    ):
        print('yes')
    else:
        print('no')
