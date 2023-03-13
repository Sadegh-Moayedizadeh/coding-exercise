from typing import List

import pytest


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def complement(number: int) -> int:
            return target - number

        numbers_to_indices = {}
        for index, number in enumerate(nums):
            if complement(number) in numbers_to_indices:
                return [index, numbers_to_indices[complement(number)]]
            numbers_to_indices[number] = index



@pytest.mark.parametrize('nums, target, expected_result', [
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([2,7,11,15], 9, [0,1])
])
def test(nums: List[int], target: int, expected_result: List[int]) -> None:
    # Arrange, Act
    actual_result = Solution().twoSum(nums, target)

    # Assert
    assert set(actual_result) == set(expected_result)
