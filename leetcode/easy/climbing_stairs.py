class Solution:
    def __init__(self) -> None:
        self._cache = {}

    def climbStairs(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]
        if n <= 2:
            return n
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self._cache[n] = result
        return result


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
