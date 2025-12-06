from functools import reduce
from result import Err, Ok, Result

from template.utils import read_input_file_as_string


def main():
    file_input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(file_input)
    print(f"{result.unwrap()}")


def solve_problem_1(file_input: list[str]) -> Result[any, str]:
    val = reduce(lambda acc, line: (lambda x,y: ((x[0]+y)%100,-~x[1] if (x[0]+y)%100 == 0 else x[1]), lambda x,y: ((x[0]-y)%100,-~x[1] if (x[0]-y)%100 == 0 else x[1]))[line[0]=="L"](acc, int(line[1:].strip())), file_input, (50,0))
    return Ok(val[1])
