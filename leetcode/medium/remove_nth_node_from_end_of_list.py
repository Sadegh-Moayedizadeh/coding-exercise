from typing import Optional
from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:
        length = self._calculate_len(head)
        if n == length:
            return head.next
        new_head = head
        i = 0
        while True:
            if i == length - n - 1:
                new_head.next = new_head.next.next
                return head
            new_head = new_head.next
            i += 1

    def _calculate_len(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        i = 0
        while head:
            head = head.next
            i += 1
        return i


print(to_list(Solution().removeNthFromEnd(to_node([1, 2, 3, 4, 5]), 5)))
