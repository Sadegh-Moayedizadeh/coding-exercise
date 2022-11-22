import pytest
from typing import List, Generic, TypeVar, Optional

ValueType = TypeVar('ValueType')


class ListNode(Generic[ValueType]):
    def __init__(
        self,
        val: ValueType = 0,
        next: Optional[ListNode] = None
    ) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode[int],
        l2: ListNode[int]
    ) -> ListNode[int]:
        first_number = self._convert_list_to_number(l1)
        second_number = self._convert_list_to_number(l2)
        return self._convert_number_into_list(first_number + second_number)

    def _convert_list_to_number(self, lst: List[int]) -> int:
        return int(''.join(map(str, lst))[::-1])

    def _convert_number_into_list(self, number) -> List[int]:
        return list(map(int, str(number)))[::-1]


@pytest.mark.parametrize('l1, l2, expected_result', [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])
def test(l1: List[int], l2: List[int], expected_result: List[int]) -> None:
    # Arrange, Act
    actual_result = Solution().addTwoNumbers(l1, l2)

    # Assert
    assert actual_result == expected_result
