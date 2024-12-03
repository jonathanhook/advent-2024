from aocd import get_data
import re

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def task(data: str) -> int:
    items: list[str] = re.findall("mul\(\d+,\d+\)", data)

    result: int = 0
    for i in items:
        parts: list[str] = i.split(',')
        a: int = int(parts[0][4:])
        b: int = int(parts[1][:-1])
        result += a * b

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 161))
    print(task(get_data(day=3, year=2024)))
main()