import codewars_test as test
from main import Node, linked_list_from_string

@test.describe("Example tests")
def example_tests():
    def each_node(head):
        while head:
            yield head
            head = head.next

    # for __repr__ and __eq__ in the assertions
    class ListReprAsLinkedList(list):
        def __repr__(self):
            return ' -> '.join(str(i) for i in self + ['None'])

    def do_one_test(expected_list, s):
        user_linked_list = linked_list_from_string(s)
        user_answer_as_arr = ListReprAsLinkedList(n.data for n in each_node(user_linked_list))
        expected_as_arr = ListReprAsLinkedList(n.data for n in each_node(expected_list))
        test.assert_equals(user_answer_as_arr, expected_as_arr)

    @test.it("basic tests")
    def basic_tests():
        head = Node(1, Node(2, Node(3)))
        do_one_test(head, "1 -> 2 -> 3 -> None")

        head = Node(0, Node(1, Node(4, Node(9, Node(16)))))
        do_one_test(head, "0 -> 1 -> 4 -> 9 -> 16 -> None")

        do_one_test(None, "None")
