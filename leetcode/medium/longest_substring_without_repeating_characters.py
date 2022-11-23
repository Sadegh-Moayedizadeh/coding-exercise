from typing import Dict
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            current_len = 0
            characters_so_far = set()
            for character in s[i:]:
                if character in characters_so_far:
                    break
                characters_so_far.add(character)
                current_len += 1
            if current_len > max_len:
                max_len = current_len
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(''))
