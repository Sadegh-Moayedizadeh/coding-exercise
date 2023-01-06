from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        is_mutable = [
            [True if element == '.' else False for element in row]
            for row in board
        ]
        value_picker = [[0] * 9 for _ in range(9)]
        i, j = 0, 0
        reverse_mode = False
        while i < 9:
            if is_mutable[i][j]:
                value = value_picker[i][j] + 1
                if value == 10:
                    reverse_mode = True
                    value_picker[i][j] = 0
                    board[i][j] = '.'
                else:
                    reverse_mode = False
                    board[i][j] = '.'
                    value_picker[i][j] = value
                    if self._is_valid(i, j, str(value), board):
                        board[i][j] = str(value)
                    else:
                        continue

            if reverse_mode:
                j -= 1
            else:
                j += 1

            if j == 9:
                i += 1
                j = 0
            elif j == -1:
                i -= 1
                j = 8

    def _is_valid(
        self, i: int, j: int, value: str, board: List[List[str]]
    ) -> bool:
        return self._is_valid_in_row(i, j, value, board) \
            and self._is_valid_in_column(i, j, value, board) \
            and self._is_valid_in_small_square(i, j, value, board)

    def _is_valid_in_row(
        self, i: int, j: int, value: str, board: List[List[str]]
    ) -> bool:
        for element in board[i]:
            if element != '.' and element == value:
                return False
        return True

    def _is_valid_in_column(
        self, i: int, j: int, value: str, board: List[List[str]]
    ) -> bool:
        return self._is_valid_in_row(j, i, value, list(map(list, zip(*board))))

    def _is_valid_in_small_square(
        self, i: int, j: int, value: str, board: List[List[str]]
    ) -> bool:
        for m in range(3 * (i // 3), 3 * (i // 3) + 3):
            for n in range(3 * (j // 3), 3 * (j // 3) + 3):
                element = board[m][n]
                if element != '.' and element == value:
                    return False
        return True


print(Solution().solveSudoku(
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
))
