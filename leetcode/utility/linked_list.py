class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def to_node(lst) -> ListNode:
    if not lst:
        return ListNode()
    head = ListNode(lst[0])
    new_head = head
    for item in lst[1:]:
        new_new_head = ListNode(item)
        new_head.next = new_new_head
        new_head = new_new_head
    return head
