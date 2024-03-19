# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        i, j = 0, 0
        characters_so_far = {}
        while j < len(s):
            if s[j] in characters_so_far and characters_so_far[s[j]] >= i:
                i = characters_so_far[s[j]] + 1
                characters_so_far[s[j]] = j
                j += 1
                continue
            characters_so_far[s[j]] = j
            if j - i + 1 > result:
                result = j - i + 1
            j += 1
        return result
