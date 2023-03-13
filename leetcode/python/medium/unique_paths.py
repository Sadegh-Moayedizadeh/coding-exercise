class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]


print(Solution().uniquePaths(3, 2))  # 3
print(Solution().uniquePaths(3, 4))  # 10
print(Solution().uniquePaths(3, 7))  # 28
