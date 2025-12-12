from result import Err, Ok, Result

from template.utils import read_input_file_as_string


def main():
    file_input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_2(file_input)
    print(f"{result.unwrap()}")


def solve_problem_2(file_input: list[str]) -> Result[any, str]:
    problem = [tuple(x.split("-")) for x in file_input[0].strip().split(",")]
    invalid_ids = []
    for start, end in problem:
        for i in range(int(start), int(end) + 1):
            x = str(i)
            rep_str = ""
            for c in x:
                if len(rep_str) > 0 and c == rep_str[0] and len(rep_str) != len(x):
                    if all(i == x.split(rep_str)[0] for i in x.split(rep_str)) and len(x.split(rep_str)) >= 3:
                        print(f"Invalid ID found: {x}")
                        invalid_ids.append(int(x))  # type: ignore
                        break
                rep_str += c
    answer = sum(invalid_ids)  # type: ignore
    return Ok(answer)
