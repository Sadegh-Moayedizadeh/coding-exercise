# https://quera.ir/problemset/80651/


def team_pick(*pairs):
    return sum(min(pair) for pair in pairs)


def get_input(num_lines):
    li = []
    res = []
    for i in range(num_lines):
        inp = int(input())
        if i%2 == 0:
            li.append(inp)
        else:
            li.append(inp)
            res.append(li)
            li = []
    return res


if __name__ == '__main__':
    pairs = get_input(num_lines=6)
    print(team_pick(*pairs))
