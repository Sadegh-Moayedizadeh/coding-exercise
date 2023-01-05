from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self._is_columns_valid(board) and \
            self._is_rows_valid(board) and \
            self._is_small_squares_valid(board)

    def _is_rows_valid(self, board: List[List[str]]) -> bool:
        for row in board:
            elements = set()
            for element in row:
                if element in elements:
                    return False
                if element != '.':
                    elements.add(element)
        return True

    def _is_columns_valid(self, board: List[List[str]]) -> bool:
        return self._is_rows_valid(list(zip(*board)))

    def _is_small_squares_valid(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                elements = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        element = board[m][n]
                        if element in elements:
                            return False
                        if element != '.':
                            elements.add(element)
        return True


print(Solution()._is_small_squares_valid(
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
))  # True
