class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next



def stringify(node: Node) -> str:
    """
    converts linked list to string
    """
    ...



if __name__ == "__main__":
    import unittest
    class TestStringify(unittest.TestCase):
        def test_empty_list(self):
            self.assertEqual(stringify(None), "None", "Failed on empty list")

        def test_single_node(self):
            node = Node(1)
            self.assertEqual(stringify(node), "1 -> None", "Failed on single node")

        def test_codewars1(self):
            self.assertEqual(stringify(Node(1, Node(2, Node(3)))), "1 -> 2 -> 3 -> None",
                             "Failed on multiple nodes")

        def test_codewars2(self):
            self.assertEqual(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))),
                             "0 -> 1 -> 4 -> 9 -> 16 -> None", "Failed on multiple nodes")

    unittest.main()
