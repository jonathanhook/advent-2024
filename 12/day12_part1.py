from aocd import get_data

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> list[list[str]]:
    return [list(l.strip()) for l in data.splitlines()]

def get_pos_info(input_grid: list[list[str]], x: int, y: int) -> tuple[str, str]:
    parts: list[str] = input_grid[y][x].split(':')
    crop: str = parts[0]
    area_label: str = ''
    if len(parts) > 1:
        area_label = parts[1]

    return crop, area_label

def calc_perimeter(input_grid: list[list[str]], x: int, y: int) -> int:
    edges: int = 0
    for p in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
        cx: int = x + p[0]
        cy: int = y + p[1]

        if cx < 0 or cx >= len(input_grid[0]) or cy < 0 or cy >= len(input_grid):
            edges += 1
            continue

        curr_info: tuple[str, str] = get_pos_info(input_grid, x, y)
        pos_info: tuple[str, str] = get_pos_info(input_grid, cx, cy)
        if pos_info[0] != curr_info[0]:
            edges += 1

    return edges


def label(input_grid: list[list[str]], x: int, y: int, crop: str, label_counter: int) -> str:
    if x < 0 or x >= len(input_grid[0]) or y < 0 or y >= len(input_grid):
        return ''

    pos_info: tuple[str, str] = get_pos_info(input_grid, x, y)
    if crop != '' and pos_info[0] != crop:
        return ''

    if pos_info[1] != '':
        return input_grid[y][x]

    new_label: str = f'{input_grid[y][x]}:{label_counter}'
    input_grid[y][x] = new_label

    for p in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
        label(input_grid, x+p[0], y+p[1], pos_info[0], label_counter)

    return new_label

def task(data: str) -> int:
    input_grid: list[list[str]] = parse_input(data)
    areas: dict[str, (int, int)] = {}
    label_counter: int = 0

    for y in range(len(input_grid)):
        for x in range(len(input_grid[0])):
            label_counter += 1
            this_label: str = label(input_grid, x, y, '', label_counter)
            perimeter: int = calc_perimeter(input_grid, x, y)

            l_area: int = 1
            l_perimeter: int = perimeter
            if this_label in areas:
                l_area = areas[this_label][0] + 1
                l_perimeter = areas[this_label][1] + perimeter
            areas[this_label] = (l_area, l_perimeter)

    result: int = 0
    for a in areas.values():
        result += a[0] * a[1]

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test1.txt'), 140))
    print(test(read_file('test2.txt'), 772))
    print(test(read_file('test3.txt'), 1930))
    print(task(get_data(day=12, year=2024)))
main()