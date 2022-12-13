from functools import reduce
from math import gcd

if __name__ == '__main__':
    number_of_numbers = int(input())
    numbers = list(map(int, input().split(' ')))
    level_of_addiction = reduce(gcd, numbers, numbers[0])
    print(sum(number//level_of_addiction for number in numbers))
