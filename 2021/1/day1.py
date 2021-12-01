from pathlib import Path


def part1(input: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(input) - 1):
    #     if input[i] < input[i + 1]:
    #         count += 1

    # oneliner
    return sum(a < b for a, b in zip(input, input[1:]))


def part2(input: list[int]) -> int:
    # more readable solution
    # count = 0
    # for i in range(len(input) - 3):
    #     if input[i] < input[i + 3]:
    #         count += 1

    # oneliner
    return sum(a < b for a, b in zip(input, input[3:]))


if __name__ == "__main__":
    puzzle = Path(__file__).parent / "input.txt"

    with puzzle.open() as f:
        puzzle: list[int] = list(map(int, f.readlines()))

    print("Part 1:", part1(puzzle))

    print("Part 2:", part2(puzzle))
