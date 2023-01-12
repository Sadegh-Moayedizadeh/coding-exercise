if __name__ == '__main__':
    h, m = map(int, input().split(' '))
    h = (12 - h) % 12
    m = (60 - m) % 60
    H = '0' + str(h) if h < 10 else str(h)
    M = '0' + str(m) if m < 10 else str(m)
    print(H + ':' + M)
