from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        _cache = {}
        def cache(func):
            def wrap(*args):
                if args in _cache:
                    return _cache[args]
                res = func(*args)
                _cache[args] = res
                return res
            return wrap
        
        @cache
        def dp(i: int, j: int) -> int:
            if i == j == 0:
                return grid[i][j]
            if i == 0:
                return dp(i, j - 1) + grid[i][j]
            if j == 0:
                return dp(i - 1, j) + grid[i][j]
            return min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]

        return dp(len(grid) - 1, len(grid[0]) - 1)


print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
print((Solution().minPathSum([[1,2,3],[4,5,6]])))  # 12
