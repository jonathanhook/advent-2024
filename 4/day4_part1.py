from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]

def search(grid: list[list[str]], x: int, y: int, dx: int, dy: int, found: str) -> int:
    sx: int = x + dx
    sy: int = y + dy

    if sx < 0 or sy < 0 or sx >= len(grid[0]) or sy >= len(grid) or len(found) > len('XMAS'):
        return 0

    found += grid[sy][sx]

    if found == 'XMAS':
        return 1
    elif found[-1] != 'XMAS'[len(found)-1]:
        return 0
    else:
        return search(grid, sx, sy, dx, dy, found)

def task(data: str) -> int:
    grid = parse_input(data)

    result: int = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'X':
                result += search(grid, x, y, 1, 0, 'X')
                result += search(grid, x, y, -1, 0, 'X')
                result += search(grid, x, y, 0, 1, 'X')
                result += search(grid, x, y, 0, -1, 'X')
                result += search(grid, x, y, 1, 1, 'X')
                result += search(grid, x, y, -1, -1, 'X')
                result += search(grid, x, y, 1, -1, 'X')
                result += search(grid, x, y, -1, 1, 'X')

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 18))
    print(task(get_data(day=4, year=2024)))
main()