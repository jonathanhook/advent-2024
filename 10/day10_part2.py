import copy
from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list:
    grid: list[list[int]] = []
    for l in data.splitlines():
        grid.append([int(char) for char in l])
    return grid

def search(grid: list[list[int]], x: int, y, last: int, path: str, reached: dict[str, bool]) -> None:
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return

    current: int = grid[y][x]
    path += f'({x},{y})'

    if current-1 != last:
        return

    if current == 9:
        reached[path] = True
        return

    search(grid, x+1, y, current, copy.deepcopy(path), reached)
    search(grid, x-1, y, current, copy.deepcopy(path), reached)
    search(grid, x, y+1, current, copy.deepcopy(path), reached)
    search(grid, x, y-1, current, copy.deepcopy(path), reached)

def task(data: str) -> int:
    grid: list[list[int]] = parse_input(data)
    result: int = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                reached: dict[str, bool] = {}
                search(grid, x, y, -1, '', reached)
                result += len(reached)

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 81))
    print(task(get_data(day=10, year=2024)))
main()