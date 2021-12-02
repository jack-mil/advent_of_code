from pathlib import Path

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
    puzzle = Path(__file__).parent / "input.txt"

    with puzzle.open() as f:
        puzzle: list[str] = f.readlines()

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))

    #$> Part 1: 2073315
    #$> Part 2: 1840311528
