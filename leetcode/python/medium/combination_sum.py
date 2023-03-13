from typing import List


class Solution:
    def __init__(self) -> None:
        self._cache = {}

    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        if target in self._cache:
            return self._cache[target]
        if target <= 0:
            return []

        result = []
        for number in candidates:
            if number == target:
                result.append([number])
            else:
                result.extend([
                    [number] + res
                    for res
                    in self.combinationSum(candidates, target - number)
                ])
        no_repetition_result = set()
        for lst in result:
            no_repetition_result.add(tuple(sorted(lst)))
        result = list(map(list, no_repetition_result))
        self._cache[target] = result
        return list(result)


print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
