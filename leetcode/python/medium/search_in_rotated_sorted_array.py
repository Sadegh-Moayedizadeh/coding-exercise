from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_point = self._find_pivot_point(nums)
        if nums[pivot_point] <= target <= nums[-1]:
            index = self._binary_search(nums[pivot_point:], target)
            if index == -1:
                return index
            return pivot_point + index
        return self._binary_search(nums[:pivot_point], target)

    def _find_pivot_point(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return mid
            elif nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[0]:
                right = mid - 1
        return 0

    def _binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
        return -1


print(Solution().search([7,8,9,1,2,3,4], 1))  # 3
print(Solution().search([1,2,3,4], 1))  # 0
print(Solution().search([7,8,9,4], 4))  # 3
print(Solution().search([4,5,6,7,0,1,2], 0))  # 4
print(Solution().search([7,8,9,1,2,3,4], 5))  # -1
print(Solution().search([5], 5))  # 0
print(Solution().search([5, 6], 5))  # 0
print(Solution().search([6, 5], 5))  # 1
print(Solution().search([6, 5], 6))  # 0

# print(Solution()._find_pivot_point([7,8,9,1,2,3,4]))  # 3
# print(Solution()._find_pivot_point([1,2,3,4]))  # 0
# print(Solution()._find_pivot_point([7,8,9,4]))  # 3
# print(Solution()._find_pivot_point([4,5,6,7,0,1,2]))  # 4
# print(Solution()._find_pivot_point([7,8,9,1,2,3,4]))  # 3
# print(Solution()._find_pivot_point([5]))  # 0
# print(Solution()._find_pivot_point([5, 6]))  # 0
# print(Solution()._find_pivot_point([6, 5]))  # 1

# print(Solution()._binary_search([1,2,3,4], 1))  # 0
# print(Solution()._binary_search([5], 5))  # 0
# print(Solution()._binary_search([5, 6], 5))  # 0
# print(Solution()._binary_search([5, 6], 6))  # 1
