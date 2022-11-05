# https://quera.org/problemset/148640/

from typing import Iterable


class Questionair:
    def __init__(self, answers: Iterable[str]) -> None:
        self._answers = answers
    
    def score(self, key: str) -> int:
        return sum(
            self._score_each(given_answer, correct_answer)
            for given_answer, correct_answer in zip(self._answers,  key)
        )

    def __repr__(self) -> str:
        return '\n'.join(self._answers)

    def _score_each(self, given_answer: str, correct_answer) -> int:
        if given_answer.count('#') == 0:
            return 0
        elif given_answer.count('#') > 1:
            return -1
        elif given_answer.index('#') == \
                self._convert_answer_letter_to_number(correct_answer):
            return 3
        else:
            return -1
    
    @staticmethod
    def _convert_answer_letter_to_number(answer_letter: str) -> int:
        if answer_letter == 'A':
            return 0
        elif answer_letter == 'B':
            return 1
        elif answer_letter == 'C':
            return 2
        elif answer_letter == 'D':
            return 3
        raise ValueError('The given answer letter is invalid.')


def main(questionairs: Iterable[Questionair], solutions) -> Iterable[int]:
    return [questionair.score(solutions) for questionair in questionairs]


def get_input() -> None:
    number_of_questions = int(input())
    solutions = input()
    number_of_qustionairs = int(input())

    questionairs = []
    given_solutions = []
    for i in range(number_of_questions * number_of_qustionairs):
        given_solutions.append(input())
        if len(given_solutions) == number_of_questions:
            questionairs.append(Questionair(given_solutions))
            given_solutions = []

    return questionairs, solutions


def print_results(scores: Iterable[int]) -> None:
    print('\n'.join(map(str, scores)))


def test() -> None:
    # Arrange
    questionair = Questionair(['OO#O', 'OOOO', '#OOO', 'OO##'])
    solutions_key = 'CABD'

    # Act
    actual_score = questionair.score(solutions_key)

    # Assert
    assert actual_score == 1


if __name__ == '__main__':
    # test()
    print_results(main(*get_input()))
