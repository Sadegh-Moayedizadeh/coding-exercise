from typing import List


class Solution:
    def __init__(self) -> None:
        self._cache = {}

    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        if target in self._cache:
            return self._cache[(target, tuple(candidates))]
        if target <= 0:
            return []

        result = []
        for number in candidates:
            if number == target:
                result.append([number])
            else:
                new_candidates = candidates.copy()
                new_candidates.remove(number)
                result.extend([
                    [number] + res
                    for res
                    in self.combinationSum2(new_candidates, target - number)
                ])
        no_repetition_result = set()
        for lst in result:
            no_repetition_result.add(tuple(sorted(lst)))
        result = list(map(list, no_repetition_result))
        self._cache[(target, tuple(candidates))] = result
        return list(result)


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
