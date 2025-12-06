from result import Err, Ok, Result

from template.utils import read_input_file_as_string


def main():
    file_input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(file_input)
    print(f"{result.unwrap()}")


def solve_problem_1(file_input: list[str]) -> Result[any, str]:
    return Err("Problem 2 not implemented yet")
