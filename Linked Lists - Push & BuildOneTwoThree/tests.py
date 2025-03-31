from main import Node, push, build_one_two_three
import codewars_test as test


@test.describe("Fixed tests")
def fxd():
    @test.it("Tests for inserting a node before another node.")
    def f():
        test.assert_equals(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
        test.assert_equals(push(None, 1).next, None, "Should be able to create a new linked list with push().")
        test.assert_equals(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
        test.assert_equals(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")

    @test.it("Tests for building a linked list.")
    def f():
        test.assert_equals(build_one_two_three().data, 1, "Value at index 0 should be 1.")
        test.assert_equals(build_one_two_three().next.data, 2, "Value at index 1 should be 2.")
        test.assert_equals(build_one_two_three().next.next.data, 3, "Value at index 2 should be 3.")
        test.assert_equals(build_one_two_three().next.next.next, None, "Value at index 3 should be null.")
