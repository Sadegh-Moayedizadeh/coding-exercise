from queue import PriorityQueue, Empty
from typing import List, Optional

from leetcode.utility import ListNode, to_list, to_node


class Value:
    def __init__(self, val: int, index: int) -> None:
        self.val = val
        self.index = index

    def __eq__(self, o):
        return self.val == o.val

    def __lt__(self, o):
        return self.val < o.val

    def __le__(self, o):
        return self.val <= o.val

    def __gt__(self, o):
        return self.val > o.val

    def __ge__(self, o):
        return self.val >= o.val


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
                q.put(Value(node.val, i))
        head = ListNode()
        new_head = head
        while True:
            try:
                value = q.get_nowait()
            except Empty:
                break

            new_head.val = value.val
            new_head.next = ListNode()
            previous_head = new_head
            new_head = new_head.next

            current_list = lists[value.index]
            current_list = current_list.next
            lists[value.index] = current_list
            if current_list:
                q.put(Value(current_list.val, value.index))
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
