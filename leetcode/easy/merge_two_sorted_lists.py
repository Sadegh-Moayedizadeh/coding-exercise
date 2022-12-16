from typing import Optional

from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)
        head = list1
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.next and head1.val <= head2.val < head1.next.val:
                new_head2 = head2.next
                new_head1_next = head1.next
                head1.next = head2
                head1.next.next = new_head1_next
                head2 = new_head2
            elif not head1.next and head2.val >= head1.val:
                head1.next = head2
                return head
            head1 = head1.next
        return head


# print(to_list(Solution().mergeTwoLists(to_node([1,2,4]), to_node([1,3,4]))))
# print(to_list(Solution().mergeTwoLists(to_node([1,2,4]), to_node([1,2,2,3,4]))))
print(to_list(Solution().mergeTwoLists(to_node([1,2,4]), to_node([3]))))
