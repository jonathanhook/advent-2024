from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> tuple[list[tuple[int, ...]], list[dict[int, int]]]:
    sections: list[str] = data.split("\n\n")
    rules: list[tuple[int, ...]] = [tuple(int(x) for x in line.split('|')) for line in sections[0].splitlines()]

    updates: list[dict[int, int]] = []
    for line in sections[1].splitlines():
        items: list[int] = [int(l) for l in line.split(',')]

        update: dict[int, int] = {}
        for i in range(len(items)):
            update[items[i]] = i
        updates.append(update)

    return rules, updates

def task(data: str) -> int:
    parsed_input = parse_input(data)
    rules: list[tuple[int, ...]] = parsed_input[0]
    updates: list[dict[int, int]] = parsed_input[1]

    result: int = 0
    for u in updates:
        passed: bool = True
        for r in rules:
            if (r[0] in u.keys() and r[1] in u.keys()) and (u[r[0]] > u[r[1]]):
                passed = False
                break

        if passed:
            keys: list[int] = list(u.keys())
            middle: int = keys[len(keys) // 2]
            result += middle

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 143))
    print(task(get_data(day=5, year=2024)))
main()