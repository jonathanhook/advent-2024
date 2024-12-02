from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list:
    return []

def task(data: str) -> int:
    return 0

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 31))
    #print(task(get_data(day=1, year=2024)))
main()