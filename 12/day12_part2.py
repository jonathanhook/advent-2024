from aocd import get_data
from mypy.applytype import apply_poly

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

def pad_input(input_grid: list[list[str]]) -> None:
    for i in range(len(input_grid)):
        input_grid[i].insert(0, '*')
        input_grid[i].append('*')

    input_grid.insert(0, ['*' for _ in range(len(input_grid[0]))])
    input_grid.append(['*' for _ in range(len(input_grid[0]))])

def rotate_kernel(k: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(y, -x) for x, y in k]

def check_vertex_instance(input_grid: list[list[str]], x: int, y: int, same: list[tuple[int, int]], diff: list[tuple[int, int]]) -> bool:
    current: str = input_grid[y][x]
    for s in same:
        checking: str = input_grid[y+s[1]][x+s[0]]
        if checking != current:
            return False

    for d in diff:
        checking: str = input_grid[y + d[1]][x + d[0]]
        if checking == current:
            return False

    return True

def create_vertices(input_grid: list[list[str]], vertices: dict[str, int]) -> None:
    for y in range(1, len(input_grid)-1):
        for x in range(1, len(input_grid[0])-1):
            val = input_grid[y][x]

            # normal corner (normal type hinting service will be resumed later)
            normal_corner = [[(1, 0), (0, 1)], [(-1, 0), (0, -1)], 1, 4]
            dead_end = [[(1, 0)],[(-1, 0), (0, 1), (0, -1)], 2, 4]
            box = [[], [(-1, 0), (0, 1), (1, 0), (0, -1)], 4, 1]

            for c in [normal_corner, dead_end, box]:
                same = c[0]
                diff = c[1]
                v_count = c[2]
                rotations = c[3]

                for _ in range(rotations):
                    found = check_vertex_instance(input_grid, x, y, same, diff)
                    if found:
                        if val in vertices:
                            vertices[val] = vertices[val] + v_count
                        else:
                            vertices[val] = v_count

                    same = rotate_kernel(same)
                    diff = rotate_kernel(diff)

def task(data: str) -> int:
    input_grid: list[list[str]] = parse_input(data)

    areas: dict[str, int] = {}
    label_counter: int = 0
    for y in range(len(input_grid)):
        for x in range(len(input_grid[0])):
            label_counter += 1
            this_label: str = label(input_grid, x, y, '', label_counter)

            if this_label in areas:
                areas[this_label] = areas[this_label] + 1
            else:
                areas[this_label] = 1

    pad_input(input_grid)
    vertices: dict[str, int] = {}
    create_vertices(input_grid, vertices)

    result: int = 0
    for k in areas.keys():
        result += areas[k] * vertices[k]

    return result

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test1.txt'), 80))
    #print(test(read_file('test2.txt'), 772))
    #print(test(read_file('test3.txt'), 1930))
    #print(task(get_data(day=12, year=2024)))
main()