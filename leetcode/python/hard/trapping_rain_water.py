from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        result = 0
        highest_in_left = self._find_max_height_until_index(heights)
        highest_in_right = list(map(
            lambda i: len(heights) - i - 1,
            self._find_max_height_until_index(heights[::-1])[::-1]
        ))
        for index in range(len(heights)):
            left_border_index = highest_in_left[index]
            right_border_index = highest_in_right[index]
            result += min(
                heights[right_border_index], heights[left_border_index]
            ) - heights[index]
        return result

    def _find_max_height_until_index(self, heights: List[int]) -> List[int]:
        result = []
        current_max_index = 0
        for index in range(len(heights)):
            if heights[index] >= heights[current_max_index]:
                current_max_index = index
            result.append(current_max_index)
        return result


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(Solution().trap([4,2,0,3,2,5]))  # 9
