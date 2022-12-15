from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        result = 0
        while i < j:
            result = max(result, self._calculate_volume(i, j, height))
            if height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return result

    def _calculate_volume(self, i: int, j: int, height: List[int]) -> int:
        if i > j:
            return self._calculate_volume(j, i, height)
        return (j - i) * min(height[i], height[j])


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
