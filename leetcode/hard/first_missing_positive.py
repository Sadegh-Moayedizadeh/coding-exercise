from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(filter(lambda n: n > 0, nums)))
        if len(nums) == 0 or nums[0] != 1:
            return 1
        target = 1
        for num in nums:
            if num != target:
                return target
            target += 1
        return target


print(Solution().firstMissingPositive([1,2,0]))  # 3
