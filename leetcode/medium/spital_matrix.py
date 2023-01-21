from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix = matrix[1:]
            matrix = list(map(list, zip(*matrix)))[::-1]
        return result


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
