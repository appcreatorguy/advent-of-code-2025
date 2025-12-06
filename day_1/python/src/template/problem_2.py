from functools import reduce
from result import Err, Ok, Result

from template.utils import read_input_file_as_string


def main():
    file_input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_2(file_input)
    print(f"{result.unwrap()}")


def solve_problem_2(file_input: list[str]) -> Result[any, str]:
    loops = 0
    counter = 50
    for line in file_input:
        amount = int(line[1:].strip())
        match line[0]:
            case "L":
                # counting down the looooong way
                for _ in range(amount):
                    counter -= 1
                    if counter == 0:
                        loops += 1
                    if counter == -1:
                        counter = 99
            case "R":
                # counting up the looooong way
                for _ in range(amount):
                    counter += 1
                    if counter == 100:
                        counter = 0
                        loops += 1
    return Ok(loops)
