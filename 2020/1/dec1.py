import os

"""
Read some numerical input from a file.
Determine the product of the 2 (or 3) entries that *sum* to 2020
"""


def part1() -> int:
    for n in nums:
        if 2020 - n in nums:
            return n * (2020 - n)
    return 0


def part2() -> int:
    for n in nums:
        for m in nums:
            if 2020 - n - m in nums:
                return n * m * (2020 - n - m)
    return 0


if __name__ == "__main__":
    me = os.path.dirname(__file__)

    with open(os.path.join(me, "input.txt")) as file:
        nums = set(map(int, file))

    print("Part 1:", part1())

    print("Part 2:", part2())
