from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 and target <= nums[mid]) \
                    or (nums[mid - 1] < target <= nums[mid]):
                return mid
            elif target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return len(nums)
