from typing import List, Optional

import pytest


class ListNode:
    def __init__(self, val = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> ListNode:
        carry = 0
        dummy_head = ListNode()
        current_node = dummy_head
        while l1 or l2 or carry:
            s = self._get_val_or_zero(l1) + self._get_val_or_zero(l2) + carry
            new_node = ListNode()
            carry = s // 10
            new_node.val = s % 10
            
            current_node.next = new_node
            current_node = new_node
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy_head.next

    def _get_val_or_zero(self, node: Optional[ListNode]) -> int:
        return node.val if node is not None else 0
