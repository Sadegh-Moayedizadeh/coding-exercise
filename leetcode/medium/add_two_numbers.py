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
        first_number = self._convert_list_to_number(
            self._convert_linked_list_to_list(l1))
        second_number = self._convert_list_to_number(
            self._convert_linked_list_to_list(l2))
        return self._convert_list_to_linked_list(
            self._convert_number_into_list(first_number + second_number))

    def _convert_linked_list_to_list(
        self,
        linked_list: ListNode[int]
    ) -> List[int]:
        result = []
        node = linked_list
        while node:
            result.append(node.val)
            node = node.next
        return result

    def _convert_list_to_linked_list(self, lst: List[int]) -> ListNode[int]:
        first_node = ListNode(val=lst[0])
        moving_node = first_node
        index = 1
        while index < len(lst):
            new_node = ListNode(val=lst[index])
            moving_node.next = new_node
            moving_node = new_node
        return first_node

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
