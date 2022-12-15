from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def to_node(lst) -> ListNode:
    head = ListNode(lst[0])
    new_head = head
    for item in lst[1:]:
        new_new_head = ListNode(item)
        new_head.next = new_new_head
        new_head = new_new_head
    return head


print(to_list(Solution().removeNthFromEnd(to_node([1, 2, 3, 4, 5]), 5)))
