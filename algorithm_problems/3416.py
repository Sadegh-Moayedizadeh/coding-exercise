from typing import List, Tuple, Iterable
import re


def compress(string: str) -> str:
    def compress_one_character(char_list: List[str]) -> str:
        if len(char_list) == 1:
            return char_list[0]
        return char_list[0] + str(len(char_list))

    char_list = []
    for char in string:
        if not char_list:
            char_list.append([char])
            continue
        if char == char_list[-1][0]:
            char_list[-1].append(char)
        else:
            char_list.append([char])
    return ''.join(map(compress_one_character, char_list))


def extract(string: str) -> str:
    def extract_one_char(string: str) -> str:
        if len(string) == 1:
            return string
        return string[0] * int(string[1:])

    pattern = r'\w\d*'
    all_matches = re.findall(pattern, string)
    return ''.join(map(extract_one_char, all_matches))


def get_inputs() -> Iterable[Tuple[str, ...]]:
    number_of_strings = int(input())
    strings = []
    for _ in range(number_of_strings):
        number = int(input())
        if number == 1:
            strings.append((input(), 'compress'))
        elif number == 2:
            strings.append((input(), 'extract'))
    return strings


if __name__ == '__main__':
    strings = get_inputs()
    for string, flag in strings:
        if flag == 'extract':
            print(extract(string))
        elif flag == 'compress':
            print(compress(string))
