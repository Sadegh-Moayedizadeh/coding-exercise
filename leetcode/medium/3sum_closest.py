from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        result = float('inf')
        k = 0
        while k < len(nums) - 2:
            i, j = k + 1, len(nums) - 1
            while i < j:
                new_candidate = nums[i] + nums[j] + nums[k]
                if new_candidate > target:
                    j -= 1
                elif new_candidate < target:
                    i += 1
                else:
                    return target
                result = min(
                    new_candidate, result, key=lambda x: abs(x - target)
                )
            k += 1
        return result


print(Solution().threeSumClosest([-1,2,1,-4], 1))
