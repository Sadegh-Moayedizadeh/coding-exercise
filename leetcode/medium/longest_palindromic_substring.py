class Solution:
    _cache = {}

    def longestPalindrome(self, s: str) -> str:
        if s in self._cache:
            return self._cache[s]
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                answer = max(
                    self.longestPalindrome(s[0: len(s)-1]),
                    self.longestPalindrome(s[1: len(s)]),
                    key=len
                )
                self._cache[s] = answer
                return answer
            i += 1
            j -= 1
        self._cache[s] = s
        return s
