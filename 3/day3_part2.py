from aocd import get_data
import re

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def multiply(mul: str) -> int:
    parts: list[str] = mul.split(',')
    a: int = int(parts[0][4:])
    b: int = int(parts[1][:-1])
    return a * b

def task(data: str) -> int:
    mul: str = "mul\(\d+,\d+\)"
    do: str = "do\(\)"
    dont: str = "don't\(\)"
    instructions: list[str] = re.compile("(%s|%s|%s)" % (mul,do,dont)).findall(data)

    result: int = 0
    state: bool = True
    for i in instructions:
        if "mul" in i and state:
            result += multiply(i)
        elif "do()" in i:
            state = True
        elif "don't()" in i:
            state = False

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 48))
    print(task(get_data(day=3, year=2024)))
main()