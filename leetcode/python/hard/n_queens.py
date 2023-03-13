from typing import List, Set, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def dfs(
            row: int,
            attacked_cells: Set[Tuple[int, int]],
            candidate_solution: List[Tuple[int, int]]
        ) -> None:
            for col in range(n):
                if (row, col) not in attacked_cells:
                    new_candidate_solution = candidate_solution + [(row, col)]
                    if row == n - 1:
                        result.append(new_candidate_solution)
                    else:
                        new_attacked_cells = attacked_cells.copy()
                        new_attacked_cells.update(
                            self._find_attacking_cells(n, row, col)
                        )
                        dfs(
                            row + 1,
                            new_attacked_cells,
                            new_candidate_solution
                        )
        dfs(0, set(), [])
        return list(map(
            list, map(
                lambda li: self._create_solution_board(n, li),
                result
            )
        ))

    def _find_attacking_cells(self, n: int, i: int, j: int) -> Set[Tuple[int, int]]:
        result = set()
        for row in range(n):
            for col in range(n):
                if row == i or col == j or abs(row - i) == abs(col - j):
                    result.add((row, col))
        return result

    def _create_solution_board(
        self, n: int, result_indices: List[Tuple[int, int]]
    ) -> List[List[str]]:
        result = []
        for row in range(n):
            new_row = []
            for col in range(n):
                if (row, col) in result_indices:
                    new_row.append('Q')
                else:
                    new_row.append('.')
            result.append(new_row)
        return map(lambda li: ''.join(li), result)


print(Solution().solveNQueens(4))
