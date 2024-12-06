import sys
from typing import Optional

from aocd import get_data
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[str]:
    return [line.strip() for line in data.splitlines()]

def get_direction(current_direction: str) -> Optional[Direction]:
    if current_direction == '^':
        return Direction.UP
    elif current_direction == '>':
        return Direction.RIGHT
    elif current_direction == 'v':
        return Direction.DOWN
    elif current_direction == '<':
        return Direction.LEFT
    else:
        return None

def step(x: int, y: int, d: Direction) -> tuple[int, int]:
    if d is Direction.UP:
        return x, y-1
    elif d is Direction.DOWN:
        return x, y+1
    elif d is Direction.LEFT:
        return x-1, y
    elif d is Direction.RIGHT:
        return x+1, y

def find_start(grid: list[str]) -> tuple[int, int, Direction]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current = get_direction(grid[j][i])
            if not current is None:
                return i, j, current

def navigate(grid: list[str], x: int, y: int, d: Direction) -> None:
    s_list = list(grid[y])
    s_list[x] = 'X'
    grid[y] = ''.join(s_list)

    n: tuple[int, int] = step(x, y, d)

    if n[0] < 0 or n[0] >= len(grid[0]) or n[1] < 0 or n[1] >= len(grid):
        return

    if grid[n[1]][n[0]] == '#':
        nd = Direction((d.value + 1) % 4)
        return navigate(grid, x, y, nd)

    return navigate(grid, n[0], n[1], d)

def task(data: str) -> int:
    grid: list[str] = parse_input(data)
    start: tuple[int, int, Direction] = find_start(grid)

    navigate(grid, start[0], start[1], start[2])

    count: int = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[j][i] == 'X':
                count += 1

    return count

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    sys.setrecursionlimit(200000)
    print(test(read_file('test.txt'), 41))
    print(task(get_data(day=6, year=2024)))
main()