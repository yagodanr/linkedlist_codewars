import codewars_test as test
from main import get_nth, Node

@test.describe("Tests")
def f():
    @test.it("tests for getting the Nth node in a linked list.")
    def v():
        linked_list = Node(1, Node(2, Node(3, None)))
        test.assert_equals(get_nth(linked_list, 0).data, 1, "First node should be located at index 0.")
        test.assert_equals(get_nth(linked_list, 1).data, 2, "Second node should be located at index 1.")
        test.assert_equals(get_nth(linked_list, 2).data, 3, "Third node should be located at index 2.")
        test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, 3))
        test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, -1))
        test.expect_error("Invalid index value should throw error.", lambda : get_nth(linked_list, 100))
        test.expect_error("None linked list should throw error.", lambda : get_nth(None, 0))