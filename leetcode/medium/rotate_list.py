from typing import Optional

from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self._calculate_length_of_list(head)
        if length in (0, 1):
            return head
        head = head
        
        tail = head
        while tail.next:
            tail = tail.next

        tail.next = head

        rounds = (length - k - 1) % length
        curr = head
        for _ in range(rounds):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head

    def _calculate_length_of_list(self, head: Optional[ListNode]) -> int:
        count = 0
        while head:
            count += 1
            head = head.next
        return count


print(to_list(Solution().rotateRight(to_node([1,2,3,4,5]), 2)))  # [4,5,1,2,3]
print(to_list(Solution().rotateRight(to_node([0,1,2]), 4)))  # [2,0,1]
