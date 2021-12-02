import os
from typing import List


def part1(answers: List[str]) -> int:
    count = 0
    unique = set()

    # Split at blank newlines
    for group in answers:
        unique.update(*group.split())
        count += len(unique)
        unique.clear()
    return count


def part2(answers: List[str]) -> int:
    count = 0
    for group in answers:
        # Find the intersection of each person's answers per group
        group_answers = [set(a) for a in group.split()]
        count += len(set.intersection(*group_answers))
    return count


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        # Split input on double newlines into groups
        answers = file.read().split("\n\n")

    print("Part 1:", part1(answers))
    print("Part 2:", part2(answers))
