from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[int]:
    return [int(i) for i in data.split()]

def count_stones(stone: int, remaining: int, cache: dict[(int, int), int]) -> int:
    if (stone, remaining) in cache:
        return cache[(stone, remaining)]

    total: int = 0
    i: int = remaining
    while i > 0:
        i-=1
        if stone == 0:
            stone = 1
        elif len(str(stone)) % 2 == 0:
            as_str = str(stone)
            left: int = int(as_str[:len(as_str)//2])
            right: int = int(as_str[len(as_str)//2:])

            total += count_stones(left, i, cache)
            total += count_stones(right, i, cache)

            cache[(stone, remaining)] = total
            return total
        else:
            stone *= 2024

    cache[(stone, remaining)] = 1
    return 1

def task(data: str, blinks: int) -> int:
    start: list[int] = parse_input(data)
    cache: dict[(int, int), int] = {}

    result: int = 0
    for s in start:
        result += count_stones(s, blinks, cache)

    return result

def test(data: str, blinks: int, expected: int) -> bool:
    result: int = task(data, blinks)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 6, 22))
    print(test(read_file('test.txt'), 25, 55312))
    print(task(get_data(day=11, year=2024), 75))
main()