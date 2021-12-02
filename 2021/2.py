from pathlib import Path
import sys

"""
Yay, a good use for python 3.10 match-case feature!
https://adventofcode.com/2021/day/2
"""


def part1(data: list[str]) -> int:
    pos = depth = 0
    for inst in data:
        match inst.split():
            # match on each instruction, split on whitespace
            case ("forward", x):
                pos += int(x)
            case ("down", x):
                depth += int(x)
            case ("up", x):
                depth -= int(x)
    return depth * pos


def part2(data: list[str]) -> int:
    pos = depth = aim = 0
    for inst in data:
        match inst.split():
            case ("forward", x):
                x = int(x)
                pos += x
                depth += aim * x
            case ("down", x):
                aim += int(x)
            case ("up", x):
                aim -= int(x)
    return depth * pos


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
        puzzle: list[str] = f.read().splitlines()

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))

    # $> Part 1: 2073315
    # $> Part 2: 1840311528
