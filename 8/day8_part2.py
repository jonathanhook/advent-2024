import math
from aocd import get_data

class Antenna:
    def __init__(self, char: str, x: int, y: int):
        self.char = char
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.char == other.char and self.x == other.x and self.y == other.y

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> tuple[list[Antenna], tuple[int, int]]:
    antennae: list[Antenna] = []
    rows: list[str] = data.splitlines()
    bounds: tuple[int, int] = (len(rows), len(rows[0]))

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            val: str = rows[i][j]
            if val != '.':
                antennae.append(Antenna(rows[i][j], j, i))

    return antennae, bounds

def find_anti_node(a: Antenna, b: Antenna, bounds: tuple[int, int]) -> list[tuple[int, int]]:
    xd: int = a.x - b.x
    yd: int = a.y - b.y

    gcd: int = math.gcd(xd, yd)
    xd = int(xd / gcd)
    yd = int(yd / gcd)

    in_bounds: bool = True
    i: int = 0
    result: list[tuple[int, int]] = []
    while in_bounds:
        ax: int = a.x + (xd * i)
        ay: int = a.y + (yd * i)
        if 0 <= ax < bounds[0] and 0 <= ay < bounds[1]:
            result.append((ax, ay))
        else:
            in_bounds = False
        i += 1

    return result

def task(data: str) -> int:
    parsed: tuple[list[Antenna], tuple[int, int]] = parse_input(data)
    antennae: list[Antenna] = parsed[0]
    bounds: tuple[int, int] = parsed[1]

    anti_nodes: list[tuple[int, int]] = []
    for a in antennae:
        for b in antennae:
            if a != b and a.char == b.char:
                an: list[tuple[int, int]] = find_anti_node(a, b, bounds)
                anti_nodes.extend(an)

    return len(set(anti_nodes))

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 34))
    print(task(get_data(day=8, year=2024)))
main()