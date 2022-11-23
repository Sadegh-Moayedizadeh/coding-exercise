import pytest
from typing import List, Optional


class ListNode:
    def __init__(
        self,
        val = 0,
        next: Optional[ListNode] = None
    ) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> ListNode:
        extra = 0
        dummy_node = ListNode()
        current_node = dummy_node
        while l1 or l2:
            s = self._get_val_or_zero(l1) + self._get_val_or_zero(l2) + extra
            new_node = ListNode()
            if s >= 10:
                extra = 1
                new_node.val = s - 10
            else:
                extra = 0
                new_node.val = s
            current_node.next = new_node
            current_node = new_node
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if extra:
            current_node.next = ListNode(1)
        return dummy_node.next

    def _get_val_or_zero(self, node: Optional[ListNode]) -> int:
        if node is None:
            return 0
        return node.val
