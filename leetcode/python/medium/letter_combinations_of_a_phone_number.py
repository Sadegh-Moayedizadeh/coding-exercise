from typing import List


class Solution:
    _digit_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for digit in digits:
            if not result:
                result = self._digit_to_letters[digit]
                continue
            new_result = []
            for string in result:
                for letter in self._digit_to_letters[digit]:
                    new_result.append(string + letter)
            result = new_result
        return result


print(Solution().letterCombinations('23'))
