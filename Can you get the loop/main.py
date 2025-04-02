class Node:
    IDS = 0
    def __init__(self, next: "Node"=None):
        self.next = next
        self.id = Node.IDS
        Node.IDS += 1

    def __repr__(self):
        def stringify(node: Node, depth: int=0) -> str:
            """
            converts linked list to string
            """
            if node is None:
                return "None"
            if depth >= 30:
                return node.id

            return f"{node.id} -> {stringify(node.next, depth+1)}"
        return stringify(self)

def loop_size(node: Node):
    if node is None or node.next is None or node.next.next is None:
        return 0

    p, fp = node, node
    p = p.next
    fp = fp.next.next
    while p != fp:
        p = p.next
        try:
            fp = fp.next.next
        except AttributeError:
            return 0

    l_size = 1
    cur = p.next
    while cur != p:
        l_size += 1
        cur = cur.next
    return l_size


nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]) == 29)
