# https://quera.org/problemset/3538/


from typing import Set

all_week_days = {
    'shanbe',
    '1shanbe',
    '2shanbe',
    '3shanbe',
    '4shanbe',
    '5shanbe',
    'jome'
}


def get_input(num_lines: int) -> Set[str]:
    result: Set[str] = set()
    for i in range(num_lines):
        inp = input()
        if i%2 == 0:
            continue
        new_set = set(inp.split(' '))
        result = result.union(new_set)
    return result


if __name__ == '__main__':
    days_with_them_present = get_input(6)
    print(len(all_week_days.difference(days_with_them_present)))
