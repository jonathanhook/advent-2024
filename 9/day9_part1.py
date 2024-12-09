import copy
from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[str]:
    return list(data)

def expand(raw: list[str]) -> list[str]:
    expanded: list[str] = []
    is_file: bool = True
    id: int = 0
    for i in range(len(raw)):
        pos: int = int(raw[i])
        for j in range(pos):
            expanded.append(str(id) if is_file else '.')
        if is_file:
            id+=1
        is_file = not is_file

    return expanded

def compress(expanded: list[str]) -> list[str]:
    s: int = 0
    e: int = len(expanded)-1

    while e-2 > s:
        while expanded[e] == '.':
            e -= 1

        while expanded[s] != '.':
            s+=1

        expanded[s] = expanded[e]
        expanded[e] = '.'

    return expanded

def checksum(compressed: list[str]) -> int:
    result: int = 0
    for i in range(len(compressed)):
        if compressed[i] == '.':
            break
        result += i * int(compressed[i])

    return result

def task(data: str) -> int:
    raw: list[str] = parse_input(data)
    expanded: list[str] = expand(raw)
    compressed: list[str] = compress(copy.deepcopy(expanded))
    result: int = checksum(compressed)

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 1928))
    print(task(get_data(day=9, year=2024)))
main()