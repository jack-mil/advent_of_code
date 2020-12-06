import os
from typing import Iterator, Optional, List


def get_id(seat: str) -> int:
    # This puzzle can be solved by interpreting the string code
    # as a binary number. The seat id is just the string with (F=0, B=1, L=0, R=1)
    chars = {'L': '0',
             'F': '0',
             'R': '1',
             'B': '1'}

    for a, b in chars.items():
        seat = seat.replace(a, b)

    # Convert from the 1-0 string to binary (base 2)
    return int(seat, 2)


def parse_seats(passes: Iterator[str]) -> List[int]:
    # Given a list of strings of the form: BFFBFBFLRL
    # convert to a set of unique seat id numbers
    return [get_id(seat.strip()) for seat in passes]


def part1(ids: List[int]) -> int:
    # Part 1 is simple the maximum of all ids
    return max(ids)


def part2(ids: List[int]) -> Optional[int]:
    # Find the sum of all theoretical ids in range [min, max]
    # The missing seat will be the difference between theoretical sum
    # and actual sum
    return sum(range(min(ids), max(ids)+1)) - sum(ids)


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        # Remove trailing newlines and create a set of seats
        ids = parse_seats(file)

    print("Part 1:", part1(ids))
    print("Part 2:", part2(ids))
