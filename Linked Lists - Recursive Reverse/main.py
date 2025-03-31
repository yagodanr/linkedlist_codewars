class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        def stringify(node: Node) -> str:
            """
            converts linked list to string
            """
            if node is None:
                return "None"

            return f"{node.data} -> {stringify(node.next)}"
        return stringify(self)

def push(head, data):
    # Your code goes here.
    if head is None:
        return Node(data)

    tmp = Node(data)
    tmp.next = head
    head = tmp

    return head

def reverse(head):
    # your code goes here.
    if head is None:
        return None

    new_head = None
    def inner(head):
        nonlocal new_head
        if head is None:
            return
        new_head = push(new_head, head.data)
        inner(head.next)
    inner(head)
    return new_head
