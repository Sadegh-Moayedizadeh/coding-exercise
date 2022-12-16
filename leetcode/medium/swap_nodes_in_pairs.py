from typing import Optional

from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        point = head
        head = head.next
        prev = None
        while point:
            if not point.next:
                break
            temp = point.next
            point.next = point.next.next
            temp.next = point
            if prev:
                prev.next = temp
            prev = point
            point = point.next
        return head


print(to_list(Solution().swapPairs(to_node([1,2,3,4, 5, 6]))))
