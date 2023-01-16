class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = self._optimize_pattern(p)
        _cache = {}
        def cache(func):
            def wrap(si, pi):
                if (si, pi) in _cache:
                    return _cache[(si, pi)]
                res = func(si, pi)
                _cache[(si, pi)] = res
                return res
            return wrap

        @cache
        def dp(si:int, pi: int) -> bool:
            if pi >= len(p) and si < len(s):
                return False
            if si >= len(s):
                if pi >= len(p):
                    return True
                if p[pi] == '*':
                    return dp(si, pi + 1)
                return False

            if s[si] != p[pi] and p[pi] not in ['*', '?']:
                return False
            if p[pi] == '*':
                return dp(si, pi + 1) or any(
                    dp(i, pi)
                    for i in range(si + 1, len(s) + 1)
                )
            return dp(si + 1, pi + 1)

        return dp(0, 0)

    def _optimize_pattern(self, p: str) -> str:
        result_list = []
        for char in p:
            if result_list and char == result_list[-1] == '*':
                continue
            result_list.append(char)
        return ''.join(result_list)


print(Solution().isMatch('aaa', 'aa?'))  # True
print(Solution().isMatch('aa', 'a'))  # False
print(Solution().isMatch('cb', '?a'))  # False
print(Solution().isMatch('cb', '*'))  # True
print(Solution().isMatch('cb', '*?'))  # True
print(Solution().isMatch('cb', '*cb'))  # True
print(Solution().isMatch('cb', '*a'))  # False
print(Solution().isMatch('abcdefg', '*c*'))  # True
print(Solution().isMatch('cdefg', 'c*fg'))  # True
print(Solution().isMatch('abcdefg', '*c****fg'))  # True
