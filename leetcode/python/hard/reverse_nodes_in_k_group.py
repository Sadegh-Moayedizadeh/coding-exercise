from typing import Optional

from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:
        fixed_prev = None
        point = head
        tail = head
        length = 1
        done = False
        while tail:
            if length == k:
                temp = tail.next
                self._reverse_sub_list(point, tail, fixed_prev)
                if not done:
                    head = tail
                    done = True
                fixed_prev = point
                point.next = temp
                point = temp
                tail = temp
                length = 0
            else:
                tail = tail.next
            length += 1
        return head

    def _reverse_sub_list(
        self,
        head: ListNode,
        tail: ListNode,
        prev: Optional[ListNode]
    ) -> None:
        point = head
        moving_prev = prev
        while point is not tail:
            temp = point.next
            point.next = moving_prev
            moving_prev = point
            point = temp
        head.next = tail.next
        tail.next = moving_prev
        if prev:
            prev.next = tail


print(to_list(Solution().reverseKGroup(to_node([1,2,3,4,5]), 3)))
