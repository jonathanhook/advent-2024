import copy
import sys
import time
from typing import Optional

from aocd import get_data
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Visited:
    def __init__(self):
        self.visits = dict()
        self.visits[Direction.UP] = False
        self.visits[Direction.DOWN] = False
        self.visits[Direction.LEFT] = False
        self.visits[Direction.RIGHT] = False

    def is_visited(self, d:Direction) -> bool:
        return self.visits[d]

    def any_visited(self):
        return self.visits[Direction.UP] or self.visits[Direction.DOWN] or self.visits[Direction.LEFT] or self.visits[Direction.RIGHT]

    def set_visit(self, d:Direction) -> None:
        self.visits[d] = True

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[list[str]]:
    return [list(line.strip()) for line in data.splitlines()]

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

def find_start(grid: list[list[str]]) -> tuple[int, int, Direction]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current = get_direction(grid[j][i])
            if not current is None:
                return i, j, current

def navigate(grid: list[list[str]], x: int, y: int, d: Direction, v: list[list[Visited]], placed: bool = False) -> int:
    v[y][x].set_visit(d)
    n: tuple[int, int] = step(x, y, d)

    # out of bounds, so not loop
    if n[0] < 0 or n[0] >= len(grid[0]) or n[1] < 0 or n[1] >= len(grid):
        return 0

    # we've hit a barrier, so turn
    nd = Direction((d.value + 1) % 4)
    if grid[n[1]][n[0]] == '#':
        return navigate(grid, x, y, nd, v, placed)

    # we've been here before in the same direction, so must be a loop
    if v[n[1]][n[0]].is_visited(d):
        return 1

    loops: int = 0
    # if not placed yet on this branch, place one
    if not placed and not v[n[1]][n[0]].any_visited():
        new_grid: list[list[str]] = copy.deepcopy(grid)
        new_grid[n[1]][n[0]] = '#'
        loops += navigate(new_grid, x, y, nd, copy.deepcopy(v), True)

    # also carry on along current route
    loops += navigate(grid, n[0], n[1], d, v, placed)

    return loops

def task(data: str) -> int:
    grid: list[list[str]] = parse_input(data)
    start: tuple[int, int, Direction] = find_start(grid)

    v: list[list[Visited]] = [[Visited() for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return navigate(grid, start[0], start[1], start[2], v)

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    start_time = time.time()
    sys.setrecursionlimit(10000)
    print(test(read_file('test.txt'), 6))
    end_time = time.time()
    print(f"{end_time - start_time:.3f} seconds")

    start_time = time.time()
    print(task(get_data(day=6, year=2024)))
    end_time = time.time()
    print(f"{end_time - start_time:.3f} seconds")
main()