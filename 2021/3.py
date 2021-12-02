from pathlib import Path


def part1(puzzle):
    pass


def part2(puzzle):
    pass


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
