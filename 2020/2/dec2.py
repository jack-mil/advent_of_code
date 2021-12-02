import os
from typing import Tuple, Set

PasswordData = Tuple[int, int, str, str]


def part1(passwords: Set[PasswordData]) -> int:
    count = 0
    for elem in passwords:
        min, max, char, paswd = elem
        if min <= paswd.count(char) <= max:
            count += 1
    return count


def part2(passwords: Set[PasswordData]) -> int:
    count = 0
    for elem in passwords:
        i, j, char, paswd = elem
        if (paswd[i - 1] == char) ^ (paswd[j - 1] == char):
            count += 1
    return count


def process_lines(lines) -> Set[PasswordData]:
    # Format: 1-3 b: cdefg
    # Convert to PasswordData format (min, max, char, password)
    data = set()
    for line in lines:
        q, char, paswd = line.replace(":", "").split()
        min, max = map(int, q.split("-"))
        data.add((min, max, char, paswd))

    return data


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        lines = process_lines(file)

    print("Part 1:", part1(lines))

    print("Part 2:", part2(lines))
