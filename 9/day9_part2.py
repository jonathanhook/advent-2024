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

def find_next_file(disk: list[str], ptr: int) -> tuple[str, int, int]:
    f_id: str = ''
    f_start = 0
    f_size: int = 0
    while ptr >= 0:
        if f_id == '' and disk[ptr] != '.':
            f_id = disk[ptr]
            f_start = ptr
            f_size = 1
        elif f_id != '':
            if disk[ptr] != f_id:
                break
            else:
                f_size += 1
                f_start -= 1

        ptr -= 1
    return f_id, f_start, f_size

def find_space(disk: list[str], f_size: int, ptr: int) -> int:
    b_start: int = -1
    b_size: int = -1
    for i in range(ptr):
        if b_start == -1 and disk[i] == '.':
            b_start = i
            b_size = 1
        elif b_start != -1 and disk[i] != '.':
            b_start = -1
        elif b_start != -1 and disk[i] == '.':
            b_size += 1

        if b_size >= f_size:
            return b_start

    return -1

def move(disk: list[str], f_start: int, f_size, b_start: int) -> None:
    for i in range(f_size):
        disk[b_start+i] = disk[f_start+i]
        disk[f_start + i] = '.'

def compress(expanded: list[str]) -> list[str]:
    ptr: int = len(expanded)-1
    while ptr > 0:
        next_f: tuple[str, int, int] = find_next_file(expanded, ptr)
        start: int = find_space(expanded, next_f[2], ptr)
        if start != -1:
            move(expanded, next_f[1], next_f[2], start)
        ptr = next_f[1]-1

    return expanded

def checksum(compressed: list[str]) -> int:
    result: int = 0
    for i in range(len(compressed)):
        if compressed[i] != '.':
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
    print(test(read_file('test.txt'), 2858))
    print(task(get_data(day=9, year=2024)))
main()