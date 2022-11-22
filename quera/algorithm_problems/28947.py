import random
from string import ascii_lowercase


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print('s' + ''.join(random.sample(ascii_lowercase, 7)))
