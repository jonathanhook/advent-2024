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
        fixed: bool = False
        pass_ok: bool = False
        while not pass_ok:
            pass_ok = True
            for r in rules:
                if (r[0] in u.keys() and r[1] in u.keys()) and (u[r[0]] > u[r[1]]):
                    tmp: int = u[r[0]]
                    u[r[0]] = u[r[1]]
                    u[r[1]] = tmp

                    pass_ok = False
                    fixed = True

        if fixed:
            sorted_keys = sorted(u.keys(), key=lambda k: u[k])
            middle: int = sorted_keys[len(sorted_keys) // 2]
            result += middle

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 123))
    print(task(get_data(day=5, year=2024)))
main()