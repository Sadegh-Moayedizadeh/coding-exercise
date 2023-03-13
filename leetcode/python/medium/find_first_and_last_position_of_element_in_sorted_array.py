from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self._find_first_occurance(nums, target),
            self._find_last_occurance(nums, target)
        ]

    def _find_first_occurance(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target \
                    and (mid == 0 or nums[mid - 1] < nums[mid]):
                return mid
            elif nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def _find_last_occurance(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target \
                    and (mid == len(nums) - 1 or nums[mid + 1] > nums[mid]):
                return mid
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
