from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []
    for l in data.splitlines():
        parts: list[str] = l.split(':')
        target: int = int(parts[0])
        values: list[int] = [int(v) for v in parts[1].split()]
        equations.append((target, values))

    return equations

def evaluate(a: int, b: int, op: str) -> int:
    if op == '+':
        return a + b
    elif op == '*':
        return a * b

def solve(target: int, equation: list[int], total: int, ptr: int, op: str) -> int:
    if ptr >= len(equation):
        if total == target:
            return target
        else: return 0

    total = evaluate(total, equation[ptr], op)
    if total > target:
        return 0

    val: int = solve(target, equation, total, ptr+1, '+')
    if val > 0:
        return val

    val = solve(target, equation, total, ptr + 1, '*')
    if val > 0:
        return val

    return 0

def task(data: str) -> int:
    equations: list[tuple[int, list[int]]] = parse_input(data)

    result: int = 0
    for e in equations:
        result += solve(e[0], e[1], 0, 0, '+')

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 3749))
    print(task(get_data(day=7, year=2024)))
main()