from pathlib import Path
from collections import deque

VALID = 0
INCOMPLETE = 1
CORRUPT = 2

pts_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
pts_2 = {")": 1, "]": 2, "}": 3, ">": 4}

# open -> close mappings
pairs = {"{": "}", "(": ")", "[": "]", "<": ">"}


def validate(line: str, ln_num: int):
    # use a deque ('deck' -- double ended queue) as a stack with the
    # .append() and .pop() methods
    stack = deque()
    for col, c in enumerate(line):
        # If this is an opening brace, add it to the stack
        if c in pairs:
            stack.append(c)
        else:
            # If a closing brace, pop the top item from the stack
            # and check it's a correct pair
            x = stack.pop()
            if c != pairs[x]:
                msg = (
                    f"Ln {ln_num}, Col {col+1}: Expected '{pairs[x]}' but found '{c}'."
                )
                return CORRUPT, c, msg

    # Check for unclosed characters
    if len(stack) > 0:
        missing = "".join([pairs[stack.pop()] for _ in range(len(stack))])
        msg = f"Ln {ln_num} incomplete: Add '{missing}'"
        return INCOMPLETE, missing, msg

    return VALID, 0, f"Ln {ln_num} valid."


def part1(lines: list[str]):
    score = 0
    for n, line in enumerate(lines):
        status, chr, msg = validate(line, n + 1)
        if status == CORRUPT:
            score += pts_1[chr]
    return score


def part2(lines: list[str]):
    total = []
    for n, line in enumerate(lines):
        score = 0
        status, missing, msg = validate(line, n + 1)
        if status == INCOMPLETE:
            for c in missing:
                score *= 5
                score += pts_2[c]
            total.append(score)
    return sorted(total)[len(total) // 2]


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

    # parse input and form a list of line segments defined by two points
    # line segments are a tuple of coordinate pairs
    with in_file.open() as f:
        lines = f.read().splitlines()

    print("Part 1:", part1(lines))

    print("Part 2:", part2(lines))

    # $> Part 1: 323613
    # $> Part 2: 3103006161
