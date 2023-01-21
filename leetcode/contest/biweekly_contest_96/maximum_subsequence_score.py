from typing import List
from itertools import combinations


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        combs = combinations(range(len(nums1)), k)
        for comb in combs:
            result = max(
                result,
                sum(nums1[i] for i in comb) * min(nums2[i] for i in comb)
            )
        return result


print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))  # 12
print(Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 1))  # 30
