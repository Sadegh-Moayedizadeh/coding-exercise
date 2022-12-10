class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return s
        start = end = 0
        for i in range(len(s)):
            l1 = self._expand_around_center(s, i, i + 1)
            l2 = self._expand_around_center(s, i, i)
            if l1 > end - start and l1 > l2:
                start = i - l1 // 2 + 1
                end = i + l1 // 2 + 1
            elif l2 > end - start:
                start = i - l2 // 2
                end = i + l2 // 2 + 1
        return s[start: end]

    def _expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
