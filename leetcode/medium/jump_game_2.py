from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
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
        def dp(i: int) -> int:
            if i == len(nums) - 1:
                return 0
            if i >= len(nums) or nums[i] == 0:
                return float('inf')
            return 1 + min(
                dp(i + j) for j in range(1, nums[i] + 1)
            )

        return dp(0)


print(Solution().jump([2,3,1,1,4]))  # 2
print(Solution().jump([2,3,0,1,4]))  # 2
