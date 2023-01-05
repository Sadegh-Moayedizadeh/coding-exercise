from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        i = 0
        while i < len(s):
            if self._is_concatenation_of_all_words(
                    s[i: i + len(words) * len(words[0])], words):
                result.append(i)
            i += 1
        return result

    def _is_concatenation_of_all_words(
        self, string: str, words: List[str]
    ) -> bool:
        word_len = len(words[0])
        words = Counter(words)
        i = 0
        while i < len(string):
            candidate = string[i: i + word_len]
            if candidate in words and words[candidate] > 0:
                words[candidate] -= 1
                i += word_len
            else:
                return False
        if all(val == 0 for val in words.values()):
            return True
        return False


print(Solution().findSubstring('barfoothefoobarman', ['foo','bar'])) # [0, 9]
print(Solution().findSubstring(
    'wordgoodgoodgoodbestword', ["word","good","best","word"]))  # []
print(Solution().findSubstring(
    'barfoofoobarthefoobarman', ["bar","foo","the"]))  # [6, 9, 12]
