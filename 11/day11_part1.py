import sys
import time
from typing import Optional
from aocd import get_data

class Stone:
    def __init__(self, v: int, p: Optional['Stone']):
        self.val: int = v
        self.prev: Optional['Stone'] = p
        self.next: Optional['Stone'] = None

    def set_next(self, n: 'Stone'):
        self.next = n

    def on_blink(self) -> None:
        if self.val == 0:
            self.val = 1
        elif len(str(self.val)) % 2 == 0:
            as_str = str(self.val)
            left: int = int(as_str[0:len(as_str)//2])
            right: int = int(as_str[len(as_str)//2:])
            self.val = left
            new_stone: Stone = Stone(right, self)
            new_stone.set_next(self.next)
            self.set_next(new_stone)
        else:
            self.val = self.val * 2024

    @staticmethod
    def get_length_from(start: 'Stone') -> int:
        count: int = 0
        current: Stone = start
        while current is not None:
            count += 1
            current = current.next
        return count

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parse_input(data: str) -> Stone:
    last: Optional[Stone] = None
    for s in data.split():
        new_stone = Stone(int(s), last)

        if last is not None:
            last.set_next(new_stone)
        last = new_stone

    head: Stone = last
    while head.prev is not None:
        head = head.prev

    return head

def task(data: str) -> int:
    head: Stone = parse_input(data)

    for i in range(25):
        current: Stone = head
        while current is not None:
            next_iter: Stone = current.next
            current.on_blink()
            current = next_iter

    return Stone.get_length_from(head)

def test(data: str, expected: int) -> bool:
    result: int = task(data)
    return result == expected

def main() -> None:
    print(test(read_file('test.txt'), 55312))
    print(task(get_data(day=11, year=2024)))
main()