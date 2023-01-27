from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        def dfs(result_so_far: List[int]) -> List[List[int]]:
            if len(result_so_far) == n:
                result.append(result_so_far)
                return
            result_set = set(result_so_far)
            for i in range(1, n+1):
                if i not in result_set:
                    dfs(result_so_far + [i])
        dfs([])
        return ''.join(map(str, result[k-1]))


print(Solution().getPermutation(3, 3))  # 213
