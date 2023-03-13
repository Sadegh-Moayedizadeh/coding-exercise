from typing import List, Set, Tuple


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result: Set[Tuple[int, int, int, int]] = set()
        nums = sorted(nums)
        a = 0
        while a < len(nums) - 3:
            k = a + 1
            while k < len(nums) - 2:
                i, j = k + 1, len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] + nums[k] + nums[a] > target:
                        j -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[a] < target:
                        i += 1
                    else:
                        result.add(
                            tuple(sorted([nums[i], nums[j], nums[k], nums[a]])))
                        j -= 1
                k += 1
            a += 1
        return list(map(list, result))



print(Solution().fourSum([1,0,-1,0,-2,2], 0))
