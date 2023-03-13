from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result = list(map(list, zip(*matrix[::-1])))
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                matrix[row][column] = result[row][column]
