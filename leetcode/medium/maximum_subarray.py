from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                result = max(s, result)
        return result


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(Solution().maxSubArray([5,4,-1,7,8]))  # 23
