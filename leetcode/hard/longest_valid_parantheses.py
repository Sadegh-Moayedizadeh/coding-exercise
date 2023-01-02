class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        i = 0
        j = 0
        score = 0
        while i < len(s):
            if j == len(s):
                i += 1
                j = i
                score = 0
                continue

            if s[j] == '(':
                score += 1
            else:
                score -= 1

            if score < 0:
                i += 1
                j = i
                score = 0
            elif score == 0:
                result = max(result, j - i + 1)
                j += 1
            else:
                j += 1
        return result


print(Solution().longestValidParentheses(')()())'))  # 4
print(Solution().longestValidParentheses('(()'))  # 2
print(Solution().longestValidParentheses(''))  # 0
