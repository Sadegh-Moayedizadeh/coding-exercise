from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    result[i][j] = 0
                elif i == j == 0:
                    result[i][j] = 1
                elif i == 0:
                    result[i][j] = result[i][j - 1]
                elif j == 0:
                    result[i][j] = result[i - 1][j]
                else:
                    result[i][j] = result[i - 1][j] + result[i][j - 1]
        
        return result[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))  # 1
print(Solution().uniquePathsWithObstacles([[1,0]]))  # 0
print(Solution().uniquePathsWithObstacles([[1]]))  # 0