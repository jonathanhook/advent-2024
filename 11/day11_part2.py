from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[int]:
    return [int(i) for i in data.split()]

def count_stones(stone: int, remaining: int, memory: dict[(int, int), int]) -> int:
    if (stone, remaining) in memory:
        return memory[stone, remaining]

    if remaining == 0:
        return 1

    if stone == 0:
        result: int = count_stones(1, remaining-1, memory)
        memory[stone, remaining] = result
        return result

    if len(str(stone)) % 2 == 0:
        as_str = str(stone)
        left: int = int(as_str[:len(as_str) // 2])
        right: int = int(as_str[len(as_str) // 2:])

        result: int = 0
        result += count_stones(left, remaining-1, memory)
        result += count_stones(right, remaining-1, memory)

        memory[stone, remaining] = result
        return result

    result: int = count_stones(stone * 2024, remaining-1, memory)
    memory[stone, remaining] = result
    return result

def task(data: str, blinks: int) -> int:
    start: list[int] = parse_input(data)
    memory: dict[(int, int), int] = {}

    result: int = 0
    for s in start:
        result += count_stones(s, blinks, memory)

    return result

def test(data: str, blinks: int, expected: int) -> bool:
    result: int = task(data, blinks)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 6, 22))
    print(test(read_file('test.txt'), 25, 55312))
    print(test(read_file('test.txt'), 75, 65601038650482))
    print(test(get_data(day=11, year=2024), 25, 194557))
    print(task(get_data(day=11, year=2024), 75))
main()