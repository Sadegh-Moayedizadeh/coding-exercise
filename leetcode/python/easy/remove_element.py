from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1
        return len(nums)


print(Solution().removeElement([1,2,3,3,4], 3))
