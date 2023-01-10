from typing import List
from collections import Counter


class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                backtrack(comb, remain - candidate, next_curr, counter, results)

                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]

        backtrack([], target, 0, counter, results)

        return results


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
