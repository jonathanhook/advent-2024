from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]

def check_kernel(grid: list[list[str]], x: int, y: int, kernel: list[list[str]]) -> int:
    for ky in range(len(kernel)):
        for kx in range(len(kernel[0])):
            val: str = kernel[ky][kx]
            if val != '.' and val != grid[x+ky-1][y+kx-1]:
                return 0

    return 1

def task(data: str) -> int:
    grid: list[list[str]] = parse_input(data)

    kernels: list = list()
    kernels.append([['M', '.', 'S'],
                    ['.', 'A', '.'],
                    ['M', '.', 'S']])

    kernels.append([['S', '.', 'M'],
                    ['.', 'A', '.'],
                    ['S', '.', 'M']])

    kernels.append([['M', '.', 'M'],
                    ['.', 'A', '.'],
                    ['S', '.', 'S']])

    kernels.append([['S', '.', 'S'],
                    ['.', 'A', '.'],
                    ['M', '.', 'M']])

    result: int = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            for k in kernels:
                result += check_kernel(grid, y, x, k)

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 9))
    print(task(get_data(day=4, year=2024)))
main()