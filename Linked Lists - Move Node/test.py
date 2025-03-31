import codewars_test as test

from main import *

@test.describe("Fixed tests")
def fxd():
    @test.it("should be able to handle two empty lists.")
    def f():
        test.expect_error("error should be thrown when source list is empty", lambda : move_node(None, None))

    @test.it("should be able to handle one empty list.")
    def f():
        test.expect_error("error should be thrown when source list is empty", lambda : move_node(None, Node(23)))
        assert_context_equals(move_node(build_one_two_three(), None), Context(build_list([2, 3]), Node(1)))

    @test.it("should be able to handle two non-empty lists.")
    def f():
        assert_context_equals(move_node(build_one_two_three(), build_one_two_three()), Context(build_list([2, 3]), build_list([1, 1, 2, 3])))
        assert_context_equals(move_node(build_one_two_three_four_five_six(), build_one_two_three_four_five_six()), Context(build_list([2, 3, 4, 5, 6]), build_list([1, 1, 2, 3, 4, 5, 6])))
        assert_context_equals(move_node(build_list([1, 2, 3, 4, 5, 6, 7]), build_list([4, 5, 6, 7])), Context(build_list([2, 3, 4, 5, 6, 7]), build_list([1, 4, 5, 6, 7])))