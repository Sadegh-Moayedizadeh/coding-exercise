# https://quera.org/problemset/108670/

from typing import List, Tuple


def remove_character_from_string(string: str, index: int) -> str:
    if index == len(string) + 1:
        return string[:index]
    return string[:index] + string[index+1:]


def first_criteria(main_word: str, candidate: str) -> bool:
    for i in range(len(candidate)):
        if main_word == remove_character_from_string(candidate, i):
            return True
    return False


def second_criteria(main_word: str, candidate: str) -> bool:
    for i in range(len(candidate)):
        if i > len(main_word) - 1:
            return False
        if remove_character_from_string(main_word, i) == remove_character_from_string(candidate, i):
            return True
    return False


def third_criteria(main_word: str, candidate: str) -> bool:
    return main_word.upper() == candidate.upper()


def main(main_words: List[str], candidates: List[str]) -> List[int]:
    result = []
    for candidate in candidates:
        matches = 0
        for main_word in main_words:
            matches += \
                first_criteria(main_word, candidate) or \
                first_criteria(candidate, main_word) or \
                second_criteria(main_word, candidate) or \
                second_criteria(candidate, main_word) or \
                third_criteria(main_word, candidate) or \
                third_criteria(candidate, main_word)
        result.append(matches)
    return result


def get_input() -> Tuple[List[str], List[str]]:
    number_of_main_words, number_of_candidates = map(int, input().split(' '))
    main_words = []
    candidates = []
    for i in range(number_of_main_words + number_of_candidates):
        if i < number_of_main_words:
            main_words.append(input())
        else:
            candidates.append(input())
    return main_words, candidates


def print_results(numbers_of_matches: List[int]) -> None:
    print('\n'.join(map(str, numbers_of_matches)))


def test_first_criteria() -> None:
    # Arrange
    main_word = 'sstem'
    candidate = 'system'

    # Act, Assert
    assert first_criteria(main_word, candidate)


def test_second_criteria() -> None:
    # Arrange
    candidate = 'pystem'
    main_word = 'system'
    
    # Act, Assert
    assert second_criteria(main_word, candidate)


def test_third_criteria() -> None:
    # Arrange
    candidate = 'hamkaran'
    main_word = 'hamKaran'

    # Act, Assert
    assert third_criteria(main_word, candidate)


def test_main() -> None:
    # Arrange
    main_words = ['hamKaran', 'system', 'systemi']
    candidates = [
        'sstem', 'hamKarani', 'hamkaran', 'hamkarani',
        'pYstem', 'pystem', 'pystemi', 'systema'
    ]
    expected_numbers_of_matches = [1, 1, 1, 0, 0, 1, 1, 2]

    # Act
    actual_numbers_of_matches = main(main_words, candidates)

    # Assert
    assert actual_numbers_of_matches == expected_numbers_of_matches, actual_numbers_of_matches


if __name__ == '__main__':
    # test_first_criteria()
    # test_second_criteria()
    # test_third_criteria()
    # test_main()
    print_results(main(*get_input()))
