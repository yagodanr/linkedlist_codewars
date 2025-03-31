class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

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

    tmp = Node(data, head)
    head = tmp

    return head

def build_one_two_three():
    # Your code goes here.
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head


def sorted_insert(head, data):
    if head is None:
        head = push(head, data)
        return head

    tmp = Node(data)
    if data < head.data:
        tmp.next = head
        head = tmp
        return head

    cur = head
    while cur is not None:
        if cur.next is None:
            cur.next = tmp
            return head

        if cur.data < data < cur.next.data:
            tmp.next = cur.next
            cur.next = tmp
            return head
        cur = cur.next
    raise Exception

