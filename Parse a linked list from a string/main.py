class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s: str) -> Node:
    elements = list(map(int, s.split(" -> ")[:-1]))
    if len(elements) == 0:
        return None

    head = Node(None)
    cur = head
    for el in elements:
        new_node = Node(el)
        cur.next = new_node
        cur = new_node
    head = head.next

    return head
