class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = s
        s2 = s[::-1]
        result = ''
        for d in range(1, len(s1) + len(s2)):
            i1 = self._positive_or_zero(len(s1) - d)
            j1 = len(s1) - self._positive_or_zero(d - len(s2))
            i2 = self._positive_or_zero(d - len(s1))
            j2 = len(s2) - self._positive_or_zero(len(s2) - d)
            sub1 = s1[i1: j1]
            sub2 = s2[i2: j2]
            
            new_result = ''
            i = 0
            for j in range(1, len(sub1) + 1):
                if sub1[i: j] == sub2[i: j]:
                    if len(sub1[i: j]) > len(new_result):
                        new_result = sub1[i: j]
                    continue
                else:
                    i = j
            if len(new_result) > len(result):
                result = new_result

        return result

    def _positive_or_zero(self, n: int) -> int:
        return 0 if n < 0 else n
