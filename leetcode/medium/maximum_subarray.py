from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = s = nums[0]
        for i in range(1, len(nums)):
            s = max(s + nums[i], nums[i])
            result = max(s, result)
        return result


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(Solution().maxSubArray([5,4,-1,7,8]))  # 23
