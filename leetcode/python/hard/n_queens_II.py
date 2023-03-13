from typing import List, Set, Tuple


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
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
        return len(result)

    def _find_attacking_cells(self, n: int, i: int, j: int) -> Set[Tuple[int, int]]:
        result = set()
        for row in range(n):
            for col in range(n):
                if row == i or col == j or abs(row - i) == abs(col - j):
                    result.add((row, col))
        return result
