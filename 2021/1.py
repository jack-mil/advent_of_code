from pathlib import Path
import sys

"""
https://adventofcode.com/2021/day/1
"""


def part1(data: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(data) - 1):
    #     if data[i] < data[i + 1]:
    #         count += 1
    # return count

    # oneliner
    return sum(a < b for a, b in zip(data, data[1:]))


def part2(data: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(data) - 3):
    #     if data[i] < data[i + 3]:
    #         count += 1
    # return count

    # oneliner
    return sum(a < b for a, b in zip(data, data[3:]))


if __name__ == "__main__":
    day = Path(__file__).stem
    # define input file name (year and day) based on directory hierarchy
    in_file = Path(f"inputs/input_{day}.txt")

    # download the file once if needed
    if not in_file.exists():
        # modify python path so we can import a module two directories up
        from util import Aoc

        print("Downloading input")
        # Download my input from the servers. Authenticated with cookies
        Aoc.yoink_input(day, file=in_file.resolve())

    print("input: ", in_file, end="\n\n")

    with in_file.open() as f:
        puzzle: list[int] = list(map(int, f.readlines()))

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))

    # $> Part 1: 1462
    # $> Part 2: 1497
