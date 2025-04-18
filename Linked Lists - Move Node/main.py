class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    tmp = source
    source = source.next
    tmp.next = dest
    dest = tmp
    return Context(source, dest)