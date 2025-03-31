class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None:
        return None

    cur = head
    while cur is not None:
        if cur.next is None:
            return head
        if cur.data == cur.next.data:
            cur.next = cur.next.next
            continue
        cur = cur.next
    raise Exception
