from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> tuple[list, list]:
    lines: list = data.splitlines()
    left: list = []
    right: list = []

    for l in lines:
        parts: list = l.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

    return left, right

def task(data: str) -> int:
    left, right = parse_input(data)
    counts: dict[int, int] = dict.fromkeys(set(left), 0)

    for r in right:
        if r in counts.keys():
            counts[r] += 1

    total: int = 0
    for l in left:
        total += l * counts[l]

    return total

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 31))
    print(task(get_data(day=1, year=2024)))
main()