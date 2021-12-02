from pathlib import Path

"""
https://adventofcode.com/2021/day/1
"""


def part1(data: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(data) - 1):
    #     if data[i] < data[i + 1]:
    #         count += 1

    # oneliner
    return sum(a < b for a, b in zip(data, data[1:]))


def part2(data: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(data) - 3):
    #     if data[i] < data[i + 3]:
    #         count += 1

    # oneliner
    return sum(a < b for a, b in zip(data, data[3:]))


if __name__ == "__main__":
    in_file: Path = Path(__file__).parent / "input.txt"

    with in_file.open() as f:
        puzzle: list[int] = list(map(int, f.readlines()))

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))

    # $> Part 1: 1462
    # $> Part 2: 1497
