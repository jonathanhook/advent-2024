import math
from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[list[int]]:
    lines = data.strip().split('\n')
    return [list(map(int, line.split())) for line in lines]

def task(data: str) -> int:
    reports: list[list[int]] = parse_input(data)
    safe_reports = 0

    for r in reports:
        last_sign: int = 0
        safe: bool = True

        for i in range(1, len(r)):
            diff: int = r[i] - r[i-1]
            sign: int = int(math.copysign(1, diff))

            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break

            if i > 1 and sign != last_sign:
                safe = False
                break

            last_sign = sign

        if safe:
            safe_reports += 1

    return safe_reports

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 2))
    print(task(get_data(day=2, year=2024)))
main()