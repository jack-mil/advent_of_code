from pathlib import Path
import util


@util.timeit()
def simulate(fish: list[int], days: int) -> int:
    """Simulates the fish population over a set number of days"""
    # hash with keys for "0"-"8"
    counts = [fish.count(i) for i in range(9)]
    counts_next = []
    for _ in range(days):
        # rotate the array
        counts_next = counts[1:] + counts[:1]
        # reset the zero fish to age 6
        counts_next[6] += counts[0]
        counts = counts_next

    return sum(counts)


def part1(fish: list[int]) -> int:
    return simulate(fish, 80)


def part2(fish: list[int]) -> int:
    return simulate(fish, 256)


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
        fish: list[int] = list(map(int, f.readline().split(",")))

    print("Part 1:", part1(fish))

    print("Part 2:", part2(fish))

    # $> Part 1: 345793
    # $> Part 2: 1572643095893
