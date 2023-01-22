if __name__ == '__main__':
    t, w = map(int, input().split(' '))
    d = t / sum(1/(2**i) for i in range(w))
    d = format(d, '.4f')
    print(d)
