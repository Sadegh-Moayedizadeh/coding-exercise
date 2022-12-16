from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        result = []
        for m in range(n):
            for left in self.generateParenthesis(m):
                for right in self.generateParenthesis(n - m - 1):
                    result.append('({}){}'.format(left, right))
        return result

print(Solution().generateParenthesis(3))
