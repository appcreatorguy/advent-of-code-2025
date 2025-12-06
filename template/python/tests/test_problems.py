from result import is_ok

from template.problem_1 import solve_problem_1
from template.problem_2 import solve_problem_2


def test_problem_1():
    file_input = open("../example.txt")

    result = solve_problem_1(file_input).unwrap()

    assert is_ok(result)
    assert result.ok_value == 0


def test_problem_2():
    file_input = open("../example.txt")

    result = solve_problem_2(file_input).unwrap()

    assert is_ok(result)
    assert result.ok_value == 0
