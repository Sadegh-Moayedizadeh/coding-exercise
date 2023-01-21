from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = index = 0
        while index <= reach:
            reach = max(index + nums[index], reach)
            if reach >= len(nums) - 1:
                return True
            index += 1
        return False
