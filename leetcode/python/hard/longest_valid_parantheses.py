class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(
            self._find_max_len(s),
            self._find_max_len(self._reverse_parantheses(s))
        )

    def _reverse_parantheses(self, s: str) -> str:
        lst = []
        for char in s[::-1]:
            if char == ')':
                lst.append('(')
            else:
                lst.append(')')
        return ''.join(lst)

    def _find_max_len(self, s: str) -> int:
        result = 0
        score = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] == '(':
                score += 1
            else:
                score -= 1

            if score == 0:
                result = max(result, j - i + 1)
                j += 1
            elif score < 0:
                score = 0
                j += 1
                i = j
            else:
                j += 1
        return result


print(Solution().longestValidParentheses(')()())'))  # 4
print(Solution().longestValidParentheses('(()'))  # 2
print(Solution().longestValidParentheses(''))  # 0
print(Solution().longestValidParentheses('()(()'))  # 2
