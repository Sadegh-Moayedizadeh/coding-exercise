from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                result = max(result, self._calculate_volume(i, j, height))
        return result

    def _calculate_volume(self, i: int, j: int, height: List[int]) -> int:
        if i > j:
            return self._calculate_volume(j, i, height)
        return (j - i) * min(height[i], height[j])


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
