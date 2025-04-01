class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    cur = head
    next = cur.next

    while next is not None:
        cur.next, next.next = next.next, cur
        cur = cur.next
        if cur is None:
            return head
        next = cur.next

    return head

