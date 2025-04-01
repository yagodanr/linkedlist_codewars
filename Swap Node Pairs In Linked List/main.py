class Node:
    IDS = 0
    def __init__(self, next=None):
        self.next = next
        self.id = Node.IDS
        Node.IDS += 1

    def __repr__(self):
        def stringify(node: Node) -> str:
            """
            converts linked list to string
            """
            if node is None:
                return "None"

            return f"{node.id} -> {stringify(node.next)}"
        return stringify(self)

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    cur = head
    head = head.next
    prev = None
    while cur is not None:
        try:
            n2 = cur.next.next
        except AttributeError:
            return head
        cur.next.next = cur
        if prev is not None:
            prev.next = cur.next
        prev = cur
        cur.next = n2
        cur = cur.next


    return head

print(swap_pairs(Node(Node(Node()))))
print(swap_pairs(Node(Node(Node(Node())))))
