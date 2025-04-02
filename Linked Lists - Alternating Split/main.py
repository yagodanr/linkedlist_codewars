class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head: Node) -> Context:
    # Your code goes here.
    # Remember to return the context.
    if head is None:
        raise Exception
    if head.next is None:
        raise Exception

    f, s = Node(head.data), Node(head.next.data)
    f_end, s_end = f, s
    add_to = [f_end, s_end]
    ind = 0

    cur = head.next.next
    while cur != None:
        new_node = Node(cur.data)
        add_to[ind].next = new_node
        add_to[ind] = add_to[ind].next
        ind = not ind
        cur = cur.next
    return Context(f, s)

