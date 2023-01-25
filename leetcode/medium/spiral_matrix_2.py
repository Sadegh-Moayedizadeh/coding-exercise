from typing import List
from enum import Enum
from pprint import pprint


class Direction(Enum):
    UP: int = 'up'
    DOWN: int = 'down'
    LEFT: int = 'left'
    RIGHT: int = 'right'


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        return self._create_matrix_from_array_in_spiral_order(
            [i for i in range(1, n**2 + 1)][::-1]
        )

    def _create_matrix_from_array_in_spiral_order(
        self, array: List[int]
    ) -> List[List[int]]:
        dimension = int(len(array)**0.5)
        result = [[0 for i in range(dimension)] for j in range(dimension)]
        i = j = 0
        direction = Direction.UP
        while True:
            if result[i][j] != 0:
                break
            result[i][j] = array.pop()
            if direction == Direction.UP:
                if i == 0 or result[i - 1][j] != 0:
                    j += 1
                    direction = direction.RIGHT
                else:
                    i -= 1
            elif direction == Direction.DOWN:
                if i == dimension - 1 or result[i + 1][j] != 0:
                    j -= 1
                    direction = direction.LEFT
                else:
                    i += 1
            elif direction == Direction.RIGHT:
                if j == dimension - 1 or result[i][j + 1] != 0:
                    i += 1
                    direction = direction.DOWN
                else:
                    j += 1
            elif direction == Direction.LEFT:
                if j == 0 or result[i][j - 1] != 0:
                    i -= 1
                    direction = direction.UP
                else:
                    j -= 1
        return result


pprint(Solution().generateMatrix(3))
pprint(Solution().generateMatrix(2))
