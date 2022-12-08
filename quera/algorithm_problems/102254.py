from collections import Counter


def extract(s: str) -> str:
    counter = Counter(s)
    if all(v == 1 for v in counter.values()):
        return s
    lst = []
    for char in counter:
        lst.append(char)
        if counter[char] != 1:
            lst.append(str(counter[char]))
    result = ''.join(sorted(lst))
    if result == ''.join(sorted(s)):
        return result
    return extract(result)
    

if __name__ == '__main__':
    print(extract(input()))
