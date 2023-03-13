from typing import Iterable, List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        result = set()
        while i < j:
            if abs(nums[i]) >= nums[j]:
                for other_two_nums in \
                        self._find_target_sum(nums[i + 1: j + 1], nums[i]):
                    result.add(tuple(sorted((nums[i],) + other_two_nums)))
                i += 1
            else:
                for other_two_nums in \
                        self._find_target_sum(nums[i: j], nums[j]):
                    result.add(tuple(sorted((nums[j],) + other_two_nums)))
                j -= 1
        if nums.count(0) >= 3:
            result.add((0, 0, 0))
        return [list(t) for t in result]

    def _find_target_sum(
        self,
        lst: List[int],
        target: int
    ) -> Iterable[Tuple[int]]:
        result = []
        i, j = 0, len(lst) - 1
        while i < j:
            if lst[i] + lst[j] + target > 0:
                j -= 1
            elif lst[i] + lst[j] + target < 0:
                i += 1
            else:
                result.append((lst[i], lst[j]))
                i += 1
                j -= 1
        return result


print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,1]))
print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([1, -1, 0, 0]))
