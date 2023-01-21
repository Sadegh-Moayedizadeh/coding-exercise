from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _cache = {}
        def cache(func):
            def wrap(i):
                if i in _cache:
                    return _cache[i]
                res = func(i)
                _cache[i] = res
                return res
            return wrap

        @cache
        def dp(index) -> bool:
            if index == len(nums) - 1:
                return True
            if index > len(nums) - 1:
                return False
            return any(dp(index + j) for j in range(nums[index], 0, -1))
        return dp(0)
