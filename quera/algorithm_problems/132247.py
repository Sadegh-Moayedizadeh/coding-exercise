from collections import Counter


def find_differece(list1, list2):
    if len(list2) > len(list1):
        return find_differece(list2, list1)

    counter = Counter(list2)
    for name in list1:
        if name not in counter or counter[name] == 0:
            return name
        else:
            counter[name] -= 1


if __name__ == '__main__':
    first_list_len = int(input())
    list1 = []
    for _ in range(first_list_len):
        list1.append(input())

    list2 = []
    for _ in range(first_list_len - 1):
        list2.append(input())

    print(find_differece(list1, list2))
