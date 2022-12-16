from queue import PriorityQueue
from typing import List, Optional

from leetcode.utility import ListNode, to_list, to_node


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        lists = list(filter(lambda n: n is not None, lists))
        if not lists:
            return None
        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i))
        head = ListNode()
        new_head = head
        while not q.empty():
            value = q.get_nowait()

            new_head.val = value[0]
            new_head.next = ListNode()
            previous_head = new_head
            new_head = new_head.next

            current_list = lists[value[1]]
            current_list = current_list.next
            lists[value[1]] = current_list
            if current_list:
                q.put((current_list.val, value[1]))
        previous_head.next = None
        return head


print(
    to_list(
        Solution().mergeKLists(
            list(map(to_node, [[1,4,5],[1,3,4],[2,6]]))
        )
    )
)

print(
    to_list(
        Solution().mergeKLists(
            list(map(to_node, [[],[1,3,4],[2,6]]))
        )
    )
)

print(
    to_list(
        Solution().mergeKLists(
            list(map(to_node, [[],[],[]]))
        )
    )
)

print(
    to_list(
        Solution().mergeKLists(
            list(map(to_node, []))
        )
    )
)

print(
    to_list(
        Solution().mergeKLists(
            list(map(to_node, [[], [1]]))
        )
    )
)
