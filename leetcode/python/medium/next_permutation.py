from typing import List, Optional


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i >= 0:
            j = self._find_smallest_numbers_index_bigger_than(
                nums[i], nums[i + 1:])
            if j is not None:
                nums[i], nums[i+ j + 1] = nums[i + j + 1], nums[i]
                self._insertion_sort_from_index(nums, i + 1)
                return nums
            i -= 1
        nums.sort()
        return nums

    def _find_smallest_numbers_index_bigger_than(
        self, n: int, nums: List[int]
    ) -> Optional[int]:
        result = None
        for i in range(len(nums)):
            if nums[i] > n:
                if result is not None and nums[i] >= nums[result]:
                    continue
                result = i
        return result

    def _insertion_sort_from_index(self, lst: List[int], index: int) -> None:
        i = index + 1
        while i < len(lst):
            if i == index or lst[i] >= lst[i - 1]:
                i += 1
            else:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                i -= 1


print(Solution().nextPermutation([1,2,3]))  # [1,3,2]
print(Solution().nextPermutation([3,2,1]))  # [1,2,3]
print(Solution().nextPermutation([1,1,5]))  # [1,5,1]
print(Solution().nextPermutation([1,3,2]))  # [2,1,3]
